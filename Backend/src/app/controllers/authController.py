import os
from datetime import datetime

import bcrypt
import jwt
import pytz
from common.utils.validators.emailValidate import valid_email
from common.utils.validators.passwordValidate import valid_password
from config.errorStatus import errorStatus
from dotenv import load_dotenv
from flask import request
from flask_restful import Resource
from jwt.exceptions import (
    DecodeError,
    ExpiredSignatureError,
    InvalidSignatureError,
    InvalidTokenError,
)
from services.authServices.createToken import (  # noqa: E501
    createAccessToken,
    createRefreshToken,
)
from sqlalchemy.orm.exc import NoResultFound

load_dotenv()

errConfig = errorStatus()

REFRESH_TOKEN_SECRET = os.getenv("REFRESH_TOKEN_SECRET")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")


# LOGIN
class login(Resource):
    def post(self):
        from app.models.userModel import Users
        from initSQL import db

        try:
            content_type = request.headers.get("Content-Type")
            if content_type == "application/json":
                json = request.get_json()
                email = json["email"]
                password = json["password"].encode("utf-8")

                # REQUIRE
                if password == "" or email == "":
                    return errConfig.msgFeedback(
                        "Please fill in email/password field!", "", 400
                    )

                # CHECK VALID EMAIL
                valid_email(email)

                valid_password(password)

                # CHECK MATCH EMAIL & PASSWORD IN DB
                User = (
                    Users.query.filter_by(email=email)
                    .options(db.defer(Users.password))
                    .one()
                )

                user_info = {
                    "user_id": User.user_id,
                    "first_name": User.first_name,
                    "last_name": User.last_name,
                    "email": User.email,
                    "avatar": User.avatar,
                    "role_id": User.role_id,
                    "address": User.address,
                    "phone": User.phone,
                    "delete_flag": User.delete_flag,
                }

                checkPW = bcrypt.checkpw(
                    password, User.password.encode("utf-8")
                )  # noqa: E501

                if not checkPW:
                    # try:
                    return errConfig.msgFeedback(
                        "Wrong password!", "", 200
                    )  # noqa: E501

                refresh_token = createRefreshToken(
                    User.user_id, User.role_id
                )  # noqa: E501

                access_token = createAccessToken(
                    User.user_id, User.role_id
                )  # noqa: E501

                refreshToken = jwt.decode(
                    refresh_token,
                    REFRESH_TOKEN_SECRET,
                    algorithms=["HS256"],
                )  # noqa: E501
                accessToken = jwt.decode(
                    access_token,
                    ACCESS_TOKEN_SECRET,
                    algorithms=["HS256"],
                )  # noqa: E501

                refreshTokenEXP = refreshToken["exp"]
                accessTokenEXP = accessToken["exp"]

                return {
                    "msg": "Login successful!",
                    "refresh_token": refresh_token,
                    "access_token": access_token,
                    "refresh_exp": refreshTokenEXP,
                    "access_exp": accessTokenEXP,
                    "user_info": user_info,
                }

            else:
                return errConfig.msgFeedback(
                    "Content-Type not support!", "", 400
                )  # noqa: E501
        except NoResultFound:
            return errConfig.msgFeedback(
                {"errorMessage": "Email or password is invalid!"}, "", 400
            )
        except Exception as e:
            return errConfig.msgFeedback(
                "Unexpected Error: ", f"{str(e)}", 500
            )  # noqa: E501


# Get ACCESS_TOKEN
class getAccessToken(Resource):
    def post(self):
        from app.models.userModel import Users

        try:
            json = request.get_json()
            refresh_token = json["refresh_token"]

            user = jwt.decode(
                refresh_token, REFRESH_TOKEN_SECRET, algorithms=["HS256"]
            )  # noqa: E501
            user_id = user["user_id"]
            print(user_id)
            refreshEXP = user["exp"]
            datetime_object_gmt7 = datetime.fromtimestamp(
                refreshEXP, tz=pytz.timezone("Asia/Ho_Chi_Minh")
            )

            currentTime = datetime.now(pytz.timezone("Asia/Ho_Chi_Minh"))

            User = Users.query.filter_by(user_id=user_id).one()

            if datetime_object_gmt7 < currentTime:
                return errConfig.msgFeedback(
                    "Expired refresh token", "", 401
                )  # noqa: E501

            if not refresh_token:
                return errConfig.msgFeedback(
                    "Please login again!", "", 401
                )  # noqa: E501

            try:
                jwt.decode(refresh_token, REFRESH_TOKEN_SECRET, "HS256")

                access_token = createAccessToken(
                    User.user_id, User.role_id
                )  # noqa: E501
                access_token_decode = jwt.decode(
                    access_token,
                    ACCESS_TOKEN_SECRET,
                    algorithms=["HS256"],  # noqa: E501
                )
                access_token_exp = access_token_decode["exp"]
                return {
                    "new_acc_token": access_token,
                    "access_token_exp": access_token_exp,
                }
            except InvalidTokenError:
                return errConfig.msgFeedback("Invalid token", "", 401)
            except DecodeError:
                return errConfig.msgFeedback(
                    "Token failed validation", "", 401
                )  # noqa: E501
            except InvalidSignatureError:
                return errConfig.msgFeedback(
                    "Invalid refresh token", "", 401
                )  # noqa: E501
            except ExpiredSignatureError:
                return errConfig.msgFeedback(
                    "The RF token is expired", "", 401
                )  # noqa: E501
            except Exception as e:
                return errConfig.msgFeedback(
                    "An unexpected error occurred decode refresh token: ",
                    f"{str(e)}",
                    500,
                )
        except Exception as e:
            return errConfig.msgFeedback(
                "Unexpected Error: ", f"{str(e)}", 500
            )  # noqa: E501


# LOGOUT
class logout(Resource):
    def get(self):
        try:
            response = errConfig.statusCode("Logout successful!")
            response.delete_cookie("RefreshToken", "/api/refresh_token")
            return response
        except Exception:
            return errConfig.statusDefault(5)

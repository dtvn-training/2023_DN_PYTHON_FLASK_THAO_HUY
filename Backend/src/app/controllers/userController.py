import os

import bcrypt
from common.utils.validators.emailValidate import valid_email
from common.utils.validators.passwordValidate import valid_password
from config.errorStatus import errorStatus
from dao.user_dao import find_user_by_email
from dotenv import load_dotenv
from flask import jsonify, request
from flask_restful import Resource
from services.authServices.auth import authMiddleware
from services.authServices.authAdmin import authMiddlewareAdmin

load_dotenv()
errConfig = errorStatus()

REFRESH_TOKEN_SECRET = os.getenv("REFRESH_TOKEN_SECRET")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")


# GET USER INFORMATION
class getUser(Resource):
    @authMiddleware
    def get(self):
        from app.models.userModel import Users
        from initSQL import db

        user_id = request.user["user_id"]

        User = (
            Users.query.filter_by(user_id=user_id)
            .options(db.defer(Users.password))
            .one_or_404()
        )

        User_dict = User.__dict__
        User_dict.pop(
            "_sa_instance_state", None
        )  # Disable _sa_instance_state of SQLAlchemy (_sa_instance_state can't convert JSON) # noqa: E501

        return jsonify(User_dict)


# GET ALL USER INFO
class getAllUser(Resource):
    @authMiddleware
    def get(self):
        from app.models.userModel import Users
        from initSQL import db

        try:
            key_word = request.args.get("key_word")
            page_number = int(request.args.get("page_number", 1))

            if key_word is None:
                key_word = ""

            limit_number_records = 3
            offset = (page_number - 1) * limit_number_records

            if not isinstance(page_number, int) or page_number < 1:
                return errConfig.msgFeedback(
                    "", {"page_number": ["Invalid page number"]}, 400
                )
            all_user_data = []

            query = Users.query.filter(
                Users.delete_flag == 0,
            ).options(db.defer(Users.password))

            if key_word == "ALL":
                user_list = (
                    query.limit(limit_number_records).offset(offset).all()
                )  # noqa: E501
                total_records = query.count()
                print(user_list)
            else:
                user_filtered = query.filter(
                    Users.first_name.like(f"%{key_word}%")
                )  # noqa: E501
                user_list = (
                    query.filter(Users.first_name.like(f"%{key_word}%"))
                    .limit(limit_number_records)
                    .offset(offset)
                    .all()
                )
                total_records = user_filtered.count()

            if user_list:
                tuple_user = [
                    {
                        "user_id": user.user_id,
                        "role_id": user.role_id,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "email": user.email,
                        "address": user.address,
                        "phone": user.phone,
                        "create_at": user.create_at,
                        "update_at": user.update_at,
                        "image": user.avatar,
                    }
                    for user in user_list
                ]
                all_user_data.append(tuple_user)
                return errConfig.msgFeedback(
                    {
                        "user_list": all_user_data,
                        "total_records": total_records,
                        "page_number": page_number,
                        "limit_number_records": limit_number_records,
                    },
                    "",
                    200,
                )
            else:
                return errConfig.msgFeedback(
                    {
                        "campaign_list": [],
                        "total_records": 0,
                        "page_number": page_number,
                        "limit_number_records": limit_number_records,
                    },
                    "No Campaign found!",
                    200,
                )
        except Exception as e:
            return errConfig.msgFeedback(
                "Unexpected Error: ", f"{str(e)}", 200
            )  # noqa: E501


# DELETE USER
class deleteUser(Resource):
    @authMiddleware
    @authMiddlewareAdmin
    def post(self):
        from app.models.userModel import Users
        from initSQL import db

        try:
            content_type = request.headers.get("Content-Type")
            if content_type == "application/json":
                json = request.get_json()
                user_id = json["user_id"]

                User = Users.query.filter_by(user_id=user_id).first()
                User.delete_flag = 1

                # db.session.delete(User)
                db.session.commit()

                return errConfig.statusCode("Delete User successfully!")
        except Exception as e:
            # return errConfig.statusDefault(4)
            return errConfig.statusCode(str(e), 500)


# ADD USER
class addUser(Resource):
    @authMiddleware
    @authMiddlewareAdmin
    def post(self):
        from app.models.userModel import Users
        from initSQL import db

        json = request.get_json()
        email = json["email"]
        first_name = json["first_name"]
        last_name = json["last_name"]
        role_id = json["role_id"]
        address = json["address"]
        phone = json["phone"]
        password = json["password"].encode("utf-8")
        try:
            valid_email(email)

            if find_user_by_email(email):
                return errConfig.msgFeedback(
                    "Email already in exist", "", 200
                )  # noqa: E501

            valid_password(password)

            hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

            user = Users(
                email=email,
                first_name=first_name,
                last_name=last_name,
                role_id=role_id,
                address=address,
                phone=phone,
                password=hashed_password,
            )
            db.session.add(user)
            db.session.commit()
            return errConfig.msgFeedback(
                "Add User successfully!", "", 200
            )  # noqa: E501
        except Exception as e:
            return errConfig.statusCode(str(e), 400)


# UPDATE USER
class updateUser(Resource):
    @authMiddleware
    @authMiddlewareAdmin
    def put(self):
        from app.models.userModel import Users
        from initSQL import db

        try:
            content_type = request.headers.get("Content-Type")
            if content_type == "application/json":
                data_acc = request.json.get(
                    "dataAcc", {}
                )  # Lấy giá trị của khóa 'dataAcc' hoặc trả về một từ điển trống nếu không tồn tại # noqa: E501
                address = data_acc.get("address")
                first_name = data_acc.get("first_name")
                last_name = data_acc.get("last_name")
                phone = data_acc.get("phone")
                role_id = data_acc.get("role_id")
                user_id = data_acc.get("user_id")

                user = Users.query.filter_by(user_id=user_id).one()
                user.address = address
                user.first_name = first_name
                user.last_name = last_name
                user.phone = phone
                user.role_id = role_id

                db.session.commit()

                return errConfig.statusCode("Update user successfully!")
        except Exception as e:
            return errConfig.statusCode(str(e), 401)


# DELETE ALL USERS
class deleteAllUser(Resource):
    @authMiddlewareAdmin
    def delete(self):
        from app.models.userModel import Users
        from initSQL import db

        try:
            db.session.query(Users).delete()
            db.session.commit()
            return errConfig.statusCode("Delete all users successfully!")
        except Exception as e:
            return errConfig.statusCode(str(e), 500)

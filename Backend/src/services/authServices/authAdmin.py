import os
from functools import wraps

import jwt
from config.errorStatus import errorStatus
from dotenv import load_dotenv
from flask import request

load_dotenv()

ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")


def authMiddlewareAdmin(func):
    @wraps(func)
    def middlewareAdmin(*args, **kwargs):
        try:
            token = request.headers.get("Authorization")
            if not token:
                return errorStatus.statusCode(
                    "Invalid Authentication.", 400
                )  # noqa: E501

            user = jwt.decode(
                token, ACCESS_TOKEN_SECRET, algorithms=["HS256"]
            )  # noqa: E501

            if user["role_id"] != "ADMIN":
                return errorStatus.statusCode(
                    "Admin resources access denied.", 500
                )  # noqa: E501
            return func(*args, **kwargs)
        except Exception as e:
            return str(e)

    return middlewareAdmin

import os
from functools import wraps

import jwt
from config.errorStatus import errorStatus
from dotenv import load_dotenv
from flask import request

# Load variables in .env environment
load_dotenv()

ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")


def authMiddleware(func):
    @wraps(func)
    def middleware(*args, **kwargs):
        try:
            token = request.headers.get("Authorization")
            if not token:
                return errorStatus.statusCode(
                    "Invalid Authentication.", 400
                )  # noqa: E501

            user = jwt.decode(
                token, ACCESS_TOKEN_SECRET, algorithms=["HS256"]
            )  # noqa: E501
            setattr(request, "user", user)
            return func(*args, **kwargs)

        except jwt.ExpiredSignatureError:
            return errorStatus.statusCode("Token has expired.", 400)
        except jwt.InvalidTokenError:
            return errorStatus.statusCode("Invalid Authentication.", 400)
        except Exception as e:
            # return errorStatus.statusCode(str(e), 500)
            return str(e)

    return middleware

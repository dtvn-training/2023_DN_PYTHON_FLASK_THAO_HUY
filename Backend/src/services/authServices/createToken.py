import os
from datetime import datetime, timedelta

import jwt
import pytz
from config.errorStatus import errorStatus
from dotenv import load_dotenv

# Load variables in .env environment
load_dotenv()
# Status code config to JSON
errConfig = errorStatus()

REFRESH_TOKEN_SECRET = os.getenv("REFRESH_TOKEN_SECRET")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")


# Create Refresh Token
def createRefreshToken(user_id, role_id):
    gmt7 = pytz.timezone("Asia/Ho_Chi_Minh")

    exp_time_gmt7 = datetime.now().astimezone(gmt7) + timedelta(days=7)
    payload = {
        "user_id": user_id,
        "role_id": role_id,
        "exp": exp_time_gmt7,
    }  # noqa: E501

    return jwt.encode(payload, REFRESH_TOKEN_SECRET, algorithm="HS256")


# Create Access Token
def createAccessToken(user_id, role_id):
    gmt7 = pytz.timezone("Asia/Ho_Chi_Minh")

    exp_time_gmt7 = datetime.now().astimezone(gmt7) + timedelta(
        minutes=15
    )  # noqa: E501

    payload = {
        "user_id": user_id,
        "role_id": role_id,
        "exp": exp_time_gmt7,
    }  # noqa: E501

    return jwt.encode(payload, ACCESS_TOKEN_SECRET, algorithm="HS256")

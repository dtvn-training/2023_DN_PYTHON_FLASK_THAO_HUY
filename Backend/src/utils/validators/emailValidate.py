import re


def validate_email(email):
    pattern = re.compile(
        r"^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$"  # noqa: E501
    )
    # Kiểm tra địa chỉ email
    return pattern.match(email) is not None

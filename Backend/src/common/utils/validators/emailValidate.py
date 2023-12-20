import re

from config.errorStatus import errorStatus

errConfig = errorStatus()


def validate_email(email):
    pattern = re.compile(
        r"^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$"  # noqa: E501
    )
    # Kiểm tra địa chỉ email
    return pattern.match(email) is not None


def valid_email(email):
    # CHECK VALID EMAIL
    try:
        if not validate_email(email):
            return errConfig.msgFeedback("Invalid email!", "", 400)

        if not isinstance(email, str):
            return errConfig.msgFeedback(
                "Email must be a string!", "", 400
            )  # noqa: E501
        # CHECK LENGTH INPUT
        if len(email) > 255:
            return errConfig.msgFeedback(
                "Email is over maximum characters", "", 400
            )  # noqa: E501
    except Exception as e:
        return errConfig.msgFeedback("", str(e), 400)

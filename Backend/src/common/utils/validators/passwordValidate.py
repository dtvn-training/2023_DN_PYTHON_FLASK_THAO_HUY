from config.errorStatus import errorStatus

errConfig = errorStatus()


def valid_password(password):
    try:
        if not isinstance(password, bytes):
            return errConfig.msgFeedback(
                "Password must be a string!", "", 400
            )  # noqa: E501
        if len(password) < 6:
            return errConfig.msgFeedback(
                "Password is over maximum characters", "", 400
            )  # noqa: E501
    except Exception as e:
        return errConfig.msgFeedback("", str(e), 400)

import app.controllers.authController as authCtrl


def initialAuthRoute(api):
    # [POST] LOGIN
    api.add_resource(authCtrl.login, "/api/login", endpoint="login")  # noqa: E501

    # [POST] GET TOKEN
    api.add_resource(
        authCtrl.getAccessToken, "/api/refresh_token", endpoint="refresh_token"
    )  # noqa: E501

    # [GET] LOGOUT
    api.add_resource(authCtrl.logout, "/api/logout", endpoint="user_logout")

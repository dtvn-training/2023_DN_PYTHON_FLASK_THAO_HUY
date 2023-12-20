import app.controllers.userController as userCtrl


def initialUserRoutes(api):
    # [GET] GET USER
    api.add_resource(userCtrl.getUser, "/api/user_info", endpoint="get_user")

    # [GET] GET ALL USERS
    api.add_resource(
        userCtrl.getAllUser, "/api/all_user_info", endpoint="get_all_user"
    )  # noqa: E501

    # [POST] ADD USER
    api.add_resource(userCtrl.addUser, "/api/add_user", endpoint="add_user")

    # [POST] UPDATE USER
    api.add_resource(
        userCtrl.updateUser, "/api/update_user", endpoint="update_user"
    )  # noqa: E501

    # [DELETE] DELETE USER
    api.add_resource(
        userCtrl.deleteUser, "/api/delete_user", endpoint="delete_user"
    )  # noqa: E501

    # [DELETE] DELETE ALL USERS
    api.add_resource(
        userCtrl.deleteAllUser,
        "/api/delete_all_user",
        endpoint="delete_all_user",  # noqa: E501
    )

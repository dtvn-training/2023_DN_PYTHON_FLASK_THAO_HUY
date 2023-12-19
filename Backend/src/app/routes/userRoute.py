from controllers.userController import (
    addUser,
    deleteAllUser,
    deleteUser,
    getAccessToken,
    getAllUser,
    getUser,
    login,
    logout,
    updateUser,
)


def initialRoutes(api):
    # [POST] LOGIN
    api.add_resource(login, "/api/login", endpoint="login")  # noqa: E501

    # [POST] GET TOKEN
    api.add_resource(
        getAccessToken, "/api/refresh_token", endpoint="refresh_token"
    )  # noqa: E501

    # [GET] LOGOUT
    api.add_resource(logout, "/api/logout", endpoint="user_logout")

    # [GET] GET USER
    api.add_resource(getUser, "/api/user_info", endpoint="get_user")

    # [GET] GET ALL USERS
    api.add_resource(
        getAllUser, "/api/all_user_info", endpoint="get_all_user"
    )  # noqa: E501

    # [POST] ADD USER
    api.add_resource(addUser, "/api/add_user", endpoint="add_user")

    # [POST] UPDATE USER
    api.add_resource(
        updateUser, "/api/update_user", endpoint="update_user"
    )  # noqa: E501

    # [DELETE] DELETE USER
    api.add_resource(
        deleteUser, "/api/delete_user", endpoint="delete_user"
    )  # noqa: E501

    # [DELETE] DELETE ALL USERS
    api.add_resource(
        deleteAllUser, "/api/delete_all_user", endpoint="delete_all_user"
    )  # noqa: E501

def find_user_by_email(email):
    from app.models.userModel import Users

    user = Users.query.filter_by(email=email).first()
    return user

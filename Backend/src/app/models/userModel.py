from datetime import datetime

from initSQL import db


class Users(db.Model):
    user_id = db.Column(db.INT, primary_key=True, autoincrement=True)
    email = db.Column(db.NVARCHAR(120), nullable=False)
    password = db.Column(db.NVARCHAR(150), nullable=False)
    first_name = db.Column(db.VARCHAR(150), nullable=False)
    last_name = db.Column(db.VARCHAR(120), nullable=False)
    role_id = db.Column(
        db.Enum("ADMIN", "DAC", "ADVERTISER"),
        db.ForeignKey("roles.role_id"),
        nullable=False,
        default="ADMIN",
    )
    address = db.Column(db.VARCHAR(255), nullable=False)
    phone = db.Column(db.VARCHAR(11), nullable=False)
    avatar = db.Column(
        db.NVARCHAR(255),
        default="https://res.cloudinary.com/dooge27kv/image/upload/v1667982724/project/avatar.png",  # noqa: E501
    )
    actions = db.Column(db.VARCHAR(150), nullable=True)
    create_at = db.Column(db.TIMESTAMP, default=datetime.now())
    update_at = db.Column(
        db.TIMESTAMP, default=datetime.now(), onupdate=datetime.now()
    )  # noqa: E501
    delete_flag = db.Column(db.BOOLEAN, default=False)

    role = db.relationship(
        "Roles", backref=db.backref("users"), lazy=True
    )  # noqa: E501

    def __init__(
        self,
        email,
        first_name,
        last_name,
        role_id,
        address,
        phone,
        password,
    ):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.role_id = role_id
        self.address = address
        self.phone = phone
        self.password = password

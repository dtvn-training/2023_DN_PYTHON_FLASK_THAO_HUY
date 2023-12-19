import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_restful import Api


def create_app():
    from initSQL import db

    app = Flask(__name__)
    api = Api(app)
    # Cross-origin
    CORS(app, supports_credentials=True)

    # Load variables in .env environment
    load_dotenv()
    DB_URL = os.getenv("DB_URL")

    app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        # from models.campaignModel import Campaigns
        # from models.creativeModel import Creatives
        # from models.rolesModel import Roles
        # from models.userModel import Users

        createTable = db.create_all()

        if createTable is not None:
            print("\n Error create models!")
        else:
            print("\n Models are all created successfully!")

    # Routes
    from routes.campaignRoute import initialRoutesCampaign
    from routes.userRoute import initialRoutes

    initialRoutes(api)
    initialRoutesCampaign(api)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(
        host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True
    )  # noqa: E501

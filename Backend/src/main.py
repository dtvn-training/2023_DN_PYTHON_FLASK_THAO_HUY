import os

from app.routes.authRoute import initialAuthRoute
from app.routes.campaignRoute import initialCampaignRoutes
from app.routes.userRoute import initialUserRoutes
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from initSQL import db

# Load variables in .env environment
load_dotenv()

app = Flask(__name__)
api = Api(app)

# Cross-origin
CORS(app, supports_credentials=True)


def create_app():
    DB_URL = os.getenv("DB_URL")

    app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        from app.models.campaignModel import Campaigns
        from app.models.creativeModel import Creatives
        from app.models.rolesModel import Roles
        from app.models.userModel import Users

        createTable = db.create_all()

        if createTable is not None:
            print("\n Error create models!")
        else:
            print("\n Models are all created successfully!")

    initialUserRoutes(api)
    initialCampaignRoutes(api)
    initialAuthRoute(api)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(
        host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True
    )  # noqa: E501

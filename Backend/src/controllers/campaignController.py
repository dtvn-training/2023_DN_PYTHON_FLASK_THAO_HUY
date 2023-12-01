import json, os, re, jwt
import bcrypt

from jwt.exceptions import *
from datetime import datetime, timedelta

from dotenv import load_dotenv

# FLASK
from flask import Flask, request, make_response, jsonify
from flask_restful import Resource, Api

# AUTH
from auth.auth import authMiddleware
from auth.authAdmin import authMiddlewareAdmin

# CONFIGS
from configs.errorStatus import errorStatus

# SERVICES
from services.campaign_service import *

# MODELS
from initSQL import db
from models.campaignModel import Campaigns
from models.userModel import Users
from models.creativeModel import Creatives

app = Flask(__name__)
api = Api(app)

# Load variables in .env environment
load_dotenv()
# Status code config to JSON
errConfig = errorStatus()

REFRESH_TOKEN_SECRET = os.getenv("REFRESH_TOKEN_SECRET")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")


# GET ALL CAMPAIGN
class getAllCampaign(Resource):
    @authMiddleware
    @authMiddlewareAdmin
    def get(self):
        campaigns = Campaigns.query.options(db.defer(Campaigns.delete_flag)).all()

        tuple_campaign = [
            {
                "user_id": campaign.user_id,
                "name": campaign.name,
                "user_status": campaign.user_status,
                "budget": campaign.budget,
                "create_at": campaign.create_at,
                "update_at": campaign.update_at,
                "bid_amount": campaign.bid_amount,
                "start_date": campaign.start_date,
                "end_date": campaign.end_date,
                "usage_rate": campaign.usage_rate,
                "campaign_id": campaign.campaign_id,
            }
            for campaign in campaigns
        ]

        return jsonify(campaigns=tuple_campaign)


# GET ONE CAMPAIGN
class getCampaign(Resource):
    @authMiddleware
    def get(self, _camp_id):
        Campaign = (
            Campaigns.query.filter_by(campaign_id=_camp_id)
            .options(db.defer(Campaigns.delete_flag))
            .first()
        )

        Campaign_dict = Campaign.__dict__
        Campaign_dict.pop(
            "_sa_instance_state", None
        )  # Disable _sa_instance_state of SQLAlchemy (_sa_instance_state can't convert JSON)

        return jsonify(Campaign_dict)


# ADD CAMPAIGN
class addCampaign(Resource):
    @authMiddleware
    @authMiddlewareAdmin
    def post(self):
        try:
            json = request.get_json()
            user_id = json["user_id"]
            name = json["name"]
            bid_amount = json["bid_amount"]
            budget = json["budget"]
            start_date = json["start_date"]
            end_date = json["end_date"]
            user_status = json["user_status"]
            title = json["title"]
            description = json["description"]
            img_preview = json["img_preview"]
            final_url = json["final_url"]

            campaign = Campaigns(
                user_id=user_id,
                name=name,
                bid_amount=int(bid_amount),
                budget=int(budget),
                start_date=start_date,
                end_date=end_date,
                user_status=user_status,
                delete_flag=True,
                used_amount=0,
                usage_rate=0,
            )
            db.session.add(campaign)
            db.session.commit()
            db.session.refresh(campaign)

            campaign_id = campaign.campaign_id
            creative = Creatives(
                campaign_id=campaign_id,
                title=title,
                description=description,
                img_preview=img_preview,
                final_url=final_url,
                delete_flag=True,
                status=True,
            )

            db.session.add(creative)
            db.session.commit()
            db.session.refresh(creative)

            if not check_date(start_date, end_date):
                return errConfig.statusCode("Invalid date", 400)

            return errConfig.statusCode("Add Campaign successfully!")
        except Exception as e:
            return errConfig.statusCode(str(e), 500)


# UPDATE CAMPAIGN
class updateCampaign(Resource):
    @authMiddleware
    def put(self):
        from initSQL import db
        from models.creativeModel import Creatives

        try:
            json = request.get_json()
            campaign_id = json["campaign_id"]
            name = json["name"]
            user_id = json["user_id"]
            bid_amount = json["bid_amount"]
            budget = json["budget"]
            start_date = json["start_date"]
            end_date = json["end_date"]
            user_status = json["user_status"]
            title = json["title"]
            description = json["description"]
            img_preview = json["img_preview"]
            final_url = json["final_url"]

            if not check_date(start_date, end_date):
                return errConfig.statusCode("Invalid date", 400)

            campaign = Campaigns.query.filter(
                Campaigns.campaign_id == campaign_id, Campaigns.user_id == user_id
            ).first()

            creative = Creatives.query.filter(
                Creatives.campaign_id == campaign_id
            ).first()

            try:
                campaign.name = name
                campaign.status = user_status
                campaign.budget = budget
                campaign.bid_amount = bid_amount
                campaign.start_date = start_date
                campaign.end_date = end_date
                # campaign.updated_at = update_at

                creative = campaign.creative
                creative.title = title
                creative.description = description
                creative.img_preview = img_preview
                creative.url = final_url
                # creative_record.updated_at = campaign_record.updated_at

                db.commit()
                db.refresh(campaign)
                # campaign_updated = update_campaign(campaign_id,user_id,name,bid_amount,budget,start_date,end_date,user_status,title,description,final_url,img_preview)

                # db.session.merge(campaign_updated)
                # db.session.commit()
                return errConfig.statusCode("Update campaign successfully!")
            except:
                return errConfig.statusCode("Update campaign failed!")
        except Exception as e:
            return errConfig.statusCode(str(e), 500)


# SEARCH CAMPAIGN BY NAME
class searchCampaignAPI(Resource):
    @authMiddleware
    def post(self):
        from initSQL import db

        try:
            json = request.get_json()
            name = json["name"]
            user_id = json["user_id"]
            start_date = json["start_date"]
            end_date = json["end_date"]

            campaign_search = search_campaign(user_id, name, start_date, end_date)
            if campaign_search:
                db.session.merge(campaign_search)
                db.session.commit()
                return errConfig.statusCode("Search campaign successfully!")
            else:
                return errConfig.statusCode("Campaign not found", 404)
        except Exception as e:
            return errConfig.statusCode(str(e), 500)


# DELETE CAMPAIGN
class deleteCampaign(Resource):
    @authMiddleware
    @authMiddlewareAdmin
    def delete(self, camp_id):

        try:
            if camp_id is None:
                return errConfig.statusCode("Invalid campaign ID", 400)

            camp = Campaigns.query.filter(Campaigns.campaign_id == camp_id).first()
            if camp:
                db.session.delete(camp)
                db.session.commit()
            return errConfig.statusCode("Delete Campaign successfully!")
        except Exception as e:
            return errConfig.statusCode(str(e), 500)

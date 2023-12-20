import os
from collections import OrderedDict
from datetime import datetime

# CONFIG
import config.errorStatus as config

# MODELS
import initSQL as dbSQL
from app.models.campaignModel import Campaigns
from app.models.creativeModel import Creatives

# SERVICES
from dao.campaign_dao import check_date

# FLASK
from flask import Flask, jsonify, request
from flask_restful import Api, Resource

# AUTH
from services.authServices.auth import authMiddleware
from services.authServices.authAdmin import authMiddlewareAdmin
from sqlalchemy import desc

app = Flask(__name__)
api = Api(app)

REFRESH_TOKEN_SECRET = os.getenv("REFRESH_TOKEN_SECRET")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")


# GET ALL CAMPAIGN
class getAllCampaign(Resource):
    @authMiddleware
    @authMiddlewareAdmin
    def get(self):
        try:
            key_word = request.args.get("key_word")
            page_number = int(request.args.get("page_number", 1))
            start_date = request.args.get("start_date")
            end_date = request.args.get("end_date")

            if key_word is None:
                key_word = ""

            limit_number_records = 3
            offset = (page_number - 1) * limit_number_records

            if not isinstance(page_number, int) or page_number < 1:
                return config.errorStatus.msgFeedback(
                    "", {"page_number": ["Invalid page number"]}, 400
                )

            all_campaign_data = []

            query = Campaigns.query.filter(
                Campaigns.delete_flag == 0,
                Campaigns.start_date >= start_date,
                Campaigns.end_date <= end_date,
            )

            if key_word == "ALL":
                campaign_list = (
                    query.limit(limit_number_records).offset(offset).all()
                )  # noqa: E501
                total_records = query.count()
            else:
                campaign_filtered = query.filter(
                    Campaigns.name.like(f"%{key_word}%")
                )  # noqa: E501
                campaign_list = (
                    query.filter(Campaigns.name.like(f"%{key_word}%"))
                    .limit(limit_number_records)
                    .offset(offset)
                    .all()
                )
                total_records = campaign_filtered.count()

            if campaign_list:
                for campaign in campaign_list:
                    creatives = Creatives.query.filter_by(
                        campaign_id=campaign.campaign_id
                    ).all()
                    tuple_creative = [
                        {
                            "creative_id": creative.creative_id,
                            "title": creative.title,
                            "description": creative.description,
                            "img_preview": creative.img_preview,
                            "final_url": creative.final_url,
                            "create_at": creative.create_at,
                            "update_at": creative.update_at,
                            "delete_flag": creative.delete_flag,
                            "campaign_id": creative.campaign_id,
                        }
                        for creative in creatives
                    ]

                    campaign_data = OrderedDict(
                        [
                            ("user_id", campaign.user_id),
                            ("name", campaign.name),
                            ("user_status", campaign.user_status),
                            ("used_amount", campaign.used_amount),
                            ("budget", campaign.budget),
                            ("status", campaign.status),
                            ("create_at", campaign.create_at),
                            ("update_at", campaign.update_at),
                            ("bid_amount", campaign.bid_amount),
                            ("start_date", str(campaign.start_date)),
                            ("end_date", str(campaign.end_date)),
                            ("usage_rate", campaign.usage_rate),
                            ("campaign_id", campaign.campaign_id),
                            ("creatives", tuple_creative),
                        ]
                    )

                    all_campaign_data.append(campaign_data)

                return config.errorStatus.msgFeedback(
                    {
                        "campaign_list": all_campaign_data,
                        "total_records": total_records,
                        "page_number": page_number,
                        "limit_number_records": limit_number_records,
                    },
                    "",
                    200,
                )

            else:
                return config.errorStatus.msgFeedback(
                    {
                        "campaign_list": [],
                        "total_records": 0,
                        "page_number": page_number,
                        "limit_number_records": limit_number_records,
                    },
                    "No Campaign found!",
                    200,
                )
        except Exception as e:
            return config.errorStatus.msgFeedback(
                "Unexpected Error: ", f"{str(e)}", 200
            )  # noqa: E501


# GET ONE CAMPAIGN
class getCampaign(Resource):
    @authMiddleware
    def get(self, _camp_id):
        try:
            Campaign = (
                Campaigns.query.filter_by(campaign_id=_camp_id)
                .options(dbSQL.db.defer(Campaigns.delete_flag))
                .first()
            )
            if Campaign:
                Campaign_dict = Campaign.__dict__
                Campaign_dict.pop(
                    "_sa_instance_state", None
                )  # Disable _sa_instance_state of SQLAlchemy (_sa_instance_state can't convert JSON) # noqa: E501

                return jsonify(Campaign_dict)
            else:
                return config.errorStatus.msgFeedback(
                    "Campaign not found!", "", 200
                )  # noqa: E501
        except Exception as e:
            return config.errorStatus.msgFeedback(
                "Unexpected Error: ", f"{str(e)}", 200
            )  # noqa: E501


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
            status = json["status"]
            user_status = json["user_status"]
            title = json["title"]
            description = json["description"]
            img_preview = json["img_preview"]
            final_url = json["final_url"]

            if not check_date(start_date, end_date):
                return config.errorStatus.msgFeedback("Invalid date", "", 200)

            if len(name) > 120 or len(name) == 0:
                return config.errorStatus.msgFeedback(
                    "Invalid name. Please re-enter", "", 200
                )  # noqa: E501

            if len(title) > 120 or len(name) == 0:
                return config.errorStatus.msgFeedback(
                    "Invalid title. Please re-enter", "", 200
                )  # noqa: E501

            if (
                len(description) > 255
                or len(img_preview) > 255
                or len(final_url) > 255
                or len(description) == 0
                or len(img_preview) == 0
                or len(final_url) == 0
                or len(bid_amount) == 0
                or len(budget) == 0
            ):
                return config.errorStatus.msgFeedback(
                    "Invalid. Please re-enter", "", 200
                )  # noqa: E501
            try:
                campaign = Campaigns(
                    user_id=user_id,
                    name=name,
                    bid_amount=bid_amount,
                    budget=budget,
                    start_date=start_date,
                    end_date=end_date,
                    status=status,
                    user_status=user_status,
                    delete_flag=False,
                    used_amount=0,
                    usage_rate=0,
                )
                dbSQL.db.session.add(campaign)
                dbSQL.db.session.commit()
                dbSQL.db.session.refresh(campaign)

                campaign_id = campaign.campaign_id
                creative = Creatives(
                    campaign_id=campaign_id,
                    title=title,
                    description=description,
                    img_preview=img_preview,
                    final_url=final_url,
                    delete_flag=False,
                )
                dbSQL.db.session.add(creative)
                dbSQL.db.session.commit()
                dbSQL.db.session.refresh(creative)
                return config.errorStatus.msgFeedback(
                    "Add Campaign successfully!", "", 200
                )  # noqa: E501
            except Exception as e:
                return config.errorStatus.msgFeedback(
                    "Add Campaign failed!", f"{str(e)}", 200
                )  # noqa: E501
        except Exception as e:
            return config.errorStatus.msgFeedback(
                "Unexpected Error: ", f"{str(e)}", 200
            )  # noqa: E501


# UPDATE CAMPAIGN BY ID
class updateCampaign(Resource):
    @authMiddleware
    def put(self, camp_id):
        try:
            json = request.get_json()
            user_id = json["user_id"]
            bid_amount = json["bid_amount"]
            budget = json["budget"]
            start_date = json["start_date"]
            end_date = json["end_date"]
            status = json["status"]
            title = json["title"]
            description = json["description"]
            img_preview = json["img_preview"]
            final_url = json["final_url"]

            if not check_date(start_date, end_date):
                return config.errorStatus.msgFeedback("Invalid date", "", 200)

            if (
                len(description) > 255
                or len(img_preview) > 255
                or len(final_url) > 255
                or len(description) == 0
                or len(img_preview) == 0
                or len(final_url) == 0
            ):
                return config.errorStatus.msgFeedback(
                    "Invalid. Please re-enter", "", 200
                )  # noqa: E501

            campaign = Campaigns.query.filter(
                Campaigns.campaign_id == camp_id, Campaigns.user_id == user_id
            ).first()

            creative = Creatives.query.filter(
                Creatives.campaign_id == camp_id
            ).first()  # noqa: E501

            try:
                campaign.budget = budget
                campaign.bid_amount = bid_amount
                campaign.start_date = start_date
                campaign.end_date = end_date
                campaign.status = status
                creative = campaign.creative
                creative.title = title
                creative.description = description
                creative.img_preview = img_preview
                creative.url = final_url

                dbSQL.db.session.commit()

                return config.errorStatus.msgFeedback(
                    "Update campaign successfully!", "", 200
                )  # noqa: E501
            except Exception as e:
                return config.errorStatus.msgFeedback(
                    "Update campaign failed!", f"{str(e)}", 200
                )
        except Exception as e:
            return config.errorStatus.msgFeedback(
                "Unexpected Error: ", f"{str(e)}", 200
            )  # noqa: E501


# DELETE CAMPAIGN
class deleteCampaign(Resource):
    @authMiddleware
    @authMiddlewareAdmin
    def delete(self, camp_id):
        try:
            if camp_id is None:
                return config.errorStatus.msgFeedback(
                    "Invalid campaign ID", "", 200
                )  # noqa: E501

            campaign = Campaigns.query.filter(
                Campaigns.campaign_id == camp_id
            ).first()  # noqa: E501
            creative = Creatives.query.filter(
                Creatives.campaign_id == camp_id
            ).first()  # noqa: E501

            if campaign:
                dbSQL.db.session.delete(campaign)
                dbSQL.db.session.delete(creative)
                dbSQL.db.session.commit()
                return config.errorStatus.msgFeedback(
                    "Delete Campaign successfully!", "", 200
                )  # noqa: E501
            else:
                return config.errorStatus.msgFeedback(
                    "Delete Campaign failed!", "", 200
                )  # noqa: E501
        except Exception as e:
            return config.errorStatus.msgFeedback(
                "Unexpected Error: ", f"{str(e)}", 200
            )  # noqa: E501


class bannerCampaign(Resource):
    def put(self, camp_id):
        try:
            json = request.get_json()
            budget = int(json["budget"])
            end_date = json["end_date"]
            bid_amount = int(json["bid_amount"])
            user_status = json["user_status"]

            if camp_id is None:
                return config.errorStatus.msgFeedback(
                    "Invalid campaign ID", "", 200
                )  # noqa: E501

            camp = Campaigns.query.filter(
                Campaigns.campaign_id == camp_id
            ).first()  # noqa: E501

            if camp:
                used_amount = camp.used_amount + bid_amount

                usage_rate = (used_amount / budget) * 100

                remain = budget - used_amount

                # return remain
                if end_date == datetime.today().date() or remain < bid_amount:
                    user_status = False

                camp.used_amount = used_amount
                camp.usage_rate = usage_rate
                camp.user_status = user_status
                dbSQL.db.session.commit()
                return config.errorStatus.msgFeedback(
                    "Update campaign successfully!", "", 200
                )  # noqa: E501
            else:
                return config.errorStatus.msgFeedback(
                    "Update campaign failed!", "", 200
                )  # noqa: E501
        except Exception as e:
            return config.errorStatus.msgFeedback(
                "Unexpected Error: ", f"{str(e)}", 200
            )  # noqa: E501


class getBannerCampaign(Resource):
    def get(self):
        try:
            campaigns = (
                Campaigns.query.filter_by(user_status=True)
                .order_by(desc(Campaigns.bid_amount))
                .limit(5)
                .all()
            )

            if campaigns:
                tuple_campaign = [
                    {
                        "name": campaign.name,
                        "user_status": campaign.user_status,
                        "bid_amount": campaign.bid_amount,
                        "campaign_id": campaign.campaign_id,
                    }
                    for campaign in campaigns
                ]
                return jsonify(campaigns=tuple_campaign)
            else:
                return config.errorStatus.statusCode("Campaign not found", 404)
        except Exception as e:
            return config.errorStatus.statusCode(str(e), 500)

import json, os,re,jwt
import bcrypt

from jwt.exceptions import *
from datetime import datetime, timedelta

from dotenv import load_dotenv
#FLASK
from flask import Flask, request, make_response,jsonify
from flask_restful import Resource, Api


from auth.auth import authMiddleware
from auth.authAdmin import authMiddlewareAdmin

from configs.errorStatus import errorStatus
from sqlalchemy.orm.exc import NoResultFound

from services.campaign_service import *

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
        from initSQL import db
        from models.campaignModel import Campaigns
        
        # json = request.get_json()
        # campaign_id = json['campaign_id']
        
        campaigns = Campaigns.query.options(db.defer(Campaigns.delete_flag)).all()
        
        tuple_campaign = [{'user_id': campaign.user_id,
                       'name': campaign.name, 
                       'user_status': campaign.user_status,
                       'budget': campaign.budget, 
                       'create_at': campaign.create_at,
                       'update_at': campaign.update_at,
                       'bid_amount': campaign.bid_amount,
                       'start_date': campaign.start_date,
                       'end_date': campaign.end_date,
                       'usage_rate': campaign.usage_rate,
                       'campaign_id': campaign.campaign_id} 
                    for campaign in campaigns]

        return jsonify(campaigns=tuple_campaign) 
    
# GET USER INFOR
class getCampaign(Resource):
    @authMiddleware
    def get_campaign_by_camp_id(self,_cam_id):
        from initSQL import db
        from models.campaignModel import Campaigns


        id = int(_cam_id)
        campaign_id = get_a_campaign_by_id(id)
        
        Campaign = Campaigns.query.filter_by(campaign_id = campaign_id).options(db.defer(Campaigns.delete_flag)).one_or_404()
        
        Campaign_dict = Campaign.__dict__
        Campaign_dict.pop('_sa_instance_state', None) # Disable _sa_instance_state of SQLAlchemy (_sa_instance_state can't convert JSON)
        
        return jsonify(Campaign_dict)
    

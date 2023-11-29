
from flask import Flask
from flask_restful import Api

from controllers.campaignController import *


def initialRoutesCampaign(api):

    # [GET] GET ALL CAMPAIGN
    api.add_resource(getAllCampaign,"/api/campaign", endpoint="campaign")

    # [GET] GET CAMPAIGN
    api.add_resource(getCampaign,"/api/campaign/<_camp_id>", endpoint="campaign")



  
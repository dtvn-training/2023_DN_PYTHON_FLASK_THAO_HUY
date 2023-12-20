import app.controllers.campaignController as campaignCtrl


def initialCampaignRoutes(api):
    # [GET] GET ALL CAMPAIGN
    api.add_resource(
        campaignCtrl.getAllCampaign, "/api/all_campaign", endpoint="campaign"
    )  # noqa: E501

    # [GET] GET CAMPAIGN
    api.add_resource(
        campaignCtrl.getCampaign,
        "/api/campaign/<_camp_id>",
        endpoint="get_campaign",  # noqa: E501
    )

    # [POST] ADD CAMPAIGN
    api.add_resource(
        campaignCtrl.addCampaign, "/api/add_campaign", endpoint="add_campaign"
    )  # noqa: E501

    # [PUT] UPDATE CAMPAIGN
    api.add_resource(
        campaignCtrl.updateCampaign,
        "/api/update_campaign/<camp_id>",
        endpoint="update_campaign",  # noqa: E501
    )

    # [POST] SHARE CAMPAIGN (UNUSED)
    # api.add_resource(searchCampaignAPI,"/api/campaign/search", endpoint="search_campaign") # noqa: E501

    # [DELETE] DELETE CAMPAIGN
    api.add_resource(
        campaignCtrl.deleteCampaign,
        "/api/delete_campaign/<camp_id>",
        endpoint="delete_campaign",  # noqa: E501
    )

    # [PUT] UPDATE BANNER CAMPAIGN
    api.add_resource(
        campaignCtrl.bannerCampaign,
        "/api/banner_campaign/<camp_id>",
        endpoint="banner_campaign",  # noqa: E501
    )

    # [GET] GET BANNER
    api.add_resource(
        campaignCtrl.getBannerCampaign,
        "/api/get_banner_campaign",
        endpoint="get_banner_campaign",  # noqa: E501
    )

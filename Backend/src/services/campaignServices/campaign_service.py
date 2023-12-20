from .campaign_dao import search_campaign_dao


def search_campaign(_user_id, _search, _start_date, _end_date):
    campaigns = search_campaign_dao(
        _user_id, _search, _start_date, _end_date
    )  # noqa: E501
    return campaigns if campaigns else None

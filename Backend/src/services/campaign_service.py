from dao.campaign_dao import *


def search_campaign(_user_id, _search, _start_date, _end_date):
    campaigns = search_campaign_dao(_user_id, _search, _start_date, _end_date)
    return campaigns if campaigns else None


def update_campaign(_id, _user_id, _name, _bid_amount, _budget, _start_date,
                    _end_date, _status, _title, _description,
                    _final_url, _preview):
    result = update_old_campaign(_id, _user_id, _name, _bid_amount, _budget,
                                 _start_date, _end_date, _status, _title,
                                 _description, _final_url, _preview)
    return result if result else None

def check_date(_start_date, _end_date):
    return _start_date <= _end_date


    





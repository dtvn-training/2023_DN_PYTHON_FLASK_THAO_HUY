from dao.campaign_dao import *


def get_all_campaign_by_user_id(user_id):
    campaigns = get_campaign_by_user_id(user_id)
    return campaigns if campaigns else None


def get_a_campaign_by_id(camp_id):
    campaign = get_camp_by_id(camp_id)
    return campaign if campaign else None


def search_campaign(_user_id, _search, _start_date, _end_date):
    campaigns = search_campaign_dao(_user_id, _search, _start_date, _end_date)
    return campaigns if campaigns else None


def insert_campaign(_user_id, _name, _bid_amount, _budget, _start_date,
                    _end_date, _status, _title, _description,
                    _final_url, _preview):
    result = insert_new_campaign(_user_id, _name, _bid_amount, _budget,
                                 _start_date, _end_date, _status, _title,
                                 _description, _final_url,  _preview)
    return result if result else None


def update_campaign(_id, _user_id, _name, _bid_amount, _budget, _start_date,
                    _end_date, _status, _title, _description,
                    _final_url, _preview):
    result = update_old_campaign(_id, _user_id, _name, _bid_amount, _budget,
                                 _start_date, _end_date, _status, _title,
                                 _description, _final_url, _preview)
    return result if result else None

def check_date(_start_date, _end_date):
    return _start_date <= _end_date


    





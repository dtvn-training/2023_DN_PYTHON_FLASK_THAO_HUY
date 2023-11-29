from models.campaignModel import Campaigns
from common.utils.images import save_preview
from initSQL import db



def get_campaign_by_user_id(_user_id):
    campaigns = Campaigns.query.filter(Campaigns.user_id == _user_id).all()
    return campaigns if campaigns else None


def get_camp_by_id(_camp_id):
    campaign = Campaigns.query.filter(Campaigns.campaign_id == _camp_id).first()
    return campaign if campaign else None


def check_date(_start_date, _end_date):
    return _end_date >= _start_date


def search_campaign_dao(_user_id, _search, _start_date, _end_date):
    if _start_date is None or _end_date is None:
        campaigns = Campaigns.query.filter(
            Campaigns.user_id == _user_id,
            Campaigns.name.like('%'+_search+'%')).all()
    else:
        campaigns = Campaigns.query.filter(
            Campaigns.user_id == _user_id,
            Campaigns.name.like('%'+_search+'%'),
            Campaigns.start_date >= _start_date,
            Campaigns.end_date <= _end_date).all()
    return campaigns if campaigns else None


def insert_new_campaign(_user_id, _name, _bid_amount, _budget, _start_date,
                        _end_date, _status, _title, _final_url, _description,
                         _preview):
    try:
        if not check_date(_start_date, _end_date):
            return None
        if _user_id is not None:
            camp = Campaigns(
                user_id=_user_id,
                name=_name,
                bid_amount=int(_bid_amount),
                budget=int(_budget),
                start_date=_start_date,
                end_date=_end_date,
                user_status=_status,
                title=_title,
                description=_description,
                img_preview=save_preview(_preview),
                final_url = _final_url
                )
            db.session.add(camp)
            db.session.commit()
            return True
    except:
        return None


def update_old_campaign(_id, _user_id, _name, _bid_amount,
                        _budget, _start_date, _end_date,
                        _status, _title, _description, 
                        _final_url, _preview):
    try:
        transaction_retrieved = Campaigns.query.filter(Campaigns.campaign_id == _id).first()
        if transaction_retrieved is not None:
            transaction_retrieved.user_id = _user_id
            transaction_retrieved.name = _name
            transaction_retrieved.bid_amount = _bid_amount
            transaction_retrieved.budget = _budget
            transaction_retrieved.start_date = _start_date
            transaction_retrieved.end_date = _end_date
            transaction_retrieved.user_status = _status
            transaction_retrieved.title = _title
            transaction_retrieved.description = _description
            transaction_retrieved.final_url = _final_url
            transaction_retrieved.img_preview = save_preview(_preview)
            db.session.commit()
            return True
    except:
        return None

    
def delete_exist_campaign(_id):
    try:
        camp = Campaigns.query.filter(Campaigns.campaign_id==_id).first()
        if camp:
            db.session.delete(camp)
            db.session.commit()
            return True
    except:
        return False 
    

    
    


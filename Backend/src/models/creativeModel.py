import uuid

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime, timedelta
from initSQL import db

class Creative(db.Model):
    creative_id = db.Column(db.NVARCHAR(16), primary_key=True,default=uuid.uuid4())
    title = db.Column(db.NVARCHAR(120), nullable=False)
    description = db.Column(db.NVARCHAR(255), nullable=False)
    img_preview = db.Column(db.VARCHAR(255), nullable=False)
    final_url = db.Column(db.NVARCHAR(255), nullable=False)
    status = db.Column(db.BOOLEAN, default=True, nullable=False)
    create_at = db.Column(db.TIMESTAMP, default=datetime.now())
    update_at = db.Column(db.TIMESTAMP, default=datetime.now(), onupdate=datetime.now())
    delete_flag = db.Column(db.BOOLEAN, default=False)
    campaign_id = db.Column(db.NVARCHAR(16), db.ForeignKey('campaign.campaign_id'), nullable=False, default=uuid.uuid4().bytes)
    
    def __init__(self,title,description,img_preview,final_url,status,delete_flag,campaign_id):
        self.title = title
        self.description = description
        self.img_preview = img_preview
        self.final_url = final_url
        self.status = status
        self.delete_flag = delete_flag
        self.campaign_id = campaign_id
import string
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#Initialize Database
db=SQLAlchemy()

class Link(db.Model):
    
    id=db.Column(db.Integer,primary_key=True)
    original_url=db.Column(db.String(512),nullable=False)
    created_at=db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self,original_url):
        self.original_url=original_url

    def generate_short_id(self):
        characters=string.digits+string.ascii_letters
        base=62
        id_num=self.id

        if id_num==0:
            return characters[0]
        
        arr=[]
        while id_num:
            id_num,rem=divmod(id_num,base)
            arr.append(characters[rem])
        arr.reverse()

        return ''.join(arr)
from app import db

class Notes(db.Document):

    title = db.StringField(required=True, max_length=126)
    description = db.StringField(required=True)
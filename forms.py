from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired()])
    photo_url = StringField("Photo", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes")
    available = BooleanField("Is this pet available?")


class EditPetForm(FlaskForm):
    photo_url = StringField("Photo", validators=[Optional(), URL()])
    notes = StringField("Notes") 








  



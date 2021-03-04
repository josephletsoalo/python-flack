from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class VehicleData(FlaskForm):
    make = StringField('Make', validators=[DataRequired()])
    model = StringField('Model', validators=[DataRequired()])
    year = StringField('Year',validators=[DataRequired()])
    color = StringField('Color',validators=[DataRequired()])
    submit = SubmitField('Submit')
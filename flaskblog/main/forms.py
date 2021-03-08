from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class SubscriptionForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()])
    submit = SubmitField('Subscribe !')
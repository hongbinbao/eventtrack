from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Email, IPAddress, Length, NumberRange, Regexp, URL, AnyOf, NoneOf, EqualTo, Optional

class NameForm(FlaskForm):
    name = StringField('name', validators=[Required()])
    submit = SubmitField('Submit')

from flask.ext.wtf import Form
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Required

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

class InceptionTableStructure(Form):
    table_name = TextAreaField('please input your table structe: ', validators=[Required()])
    submit = SubmitField('Submit')
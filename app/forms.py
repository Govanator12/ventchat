from flask_wtf import FlaskForm
from flask import flash
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, length

class ContactForm(FlaskForm):
    name = StringField('Name')
    email = StringField("E-mail",validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired(), length(max=500)])
    submit = SubmitField('Contact')

class PostForm(FlaskForm):
    message = TextAreaField('Type a message...', validators=[DataRequired(), length(max=500)])
    submit = SubmitField('Send')

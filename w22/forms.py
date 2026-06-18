from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Ім’я користувача', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Увійти')

class MessageForm(FlaskForm):
    message = TextAreaField('Ваше повідомлення', validators=[DataRequired()])
    submit = SubmitField('Відправити')
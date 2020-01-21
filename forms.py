from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

## using wtforms - create python classes that translate into html
class RegistrationForm(FlaskForm):
    # username field, required, with length btwn 2 and 20
    username = StringField('Username', validators = [DataRequired(), Length(min = 3, max = 20)]);

    # email field, required
    email = StringField('Email', validators = [DataRequired(), Email()])

    password = PasswordField('Password', validators = [DataRequired()])

    # use EqualTo to check the password is the same as the above password
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])

    submit = SubmitField('Signup')


class LoginForm(FlaskForm):
    
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)]);

    password = PasswordField('Password', validators=[DataRequired()])

    remember = BooleanField('Remember me!')
    submit = SubmitField('Login')

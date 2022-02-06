from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class WFMHRegistrationForm(FlaskForm):

    # def validate_username(self, username_to_check):
    #     user_already_registered = User.query.filter_by(
    #         username=username_to_check.data).first()
    #     if user_already_registered:
    #         raise ValidationError(
    #             'That username is already registered! Please try again with a different username.')

    # def validate_email_address(self, email_address_to_check):
    #     email_already_registered = User.query.filter_by(
    #         email_address=email_address_to_check.data).first()
    #     if email_already_registered:
    #         raise ValidationError(
    #             'That email is already registered! Please try again with a different email address.')

    r_profile_name = StringField(label='enter profile name')
    r_email = StringField(label='enter email')
    r_password = PasswordField(
        label='enter password')
    r_password_confirm = PasswordField(label='confirm password')
    submit = SubmitField(label='REGISTER')

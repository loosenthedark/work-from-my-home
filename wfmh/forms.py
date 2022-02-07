from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError

from wfmh.models import Worker


class WFMHRegistrationForm(FlaskForm):

    def validate_r_profile_name(self, new_user):
        previously_registered_user = Worker.query.filter_by(
            profile_name=new_user.data).first()
        if previously_registered_user:
            raise ValidationError(
                'That username is already registered! Please try again with a different username.')

    def validate_r_email(self, new_email):
        previously_registered_email = Worker.query.filter_by(
            worker_email=new_email.data).first()
        if previously_registered_email:
            raise ValidationError(
                'That email is already registered! Please try again with a different email address.')

    r_profile_name = StringField(label='Enter profile name', validators=[Length(min=3, max=20), DataRequired()])
    r_email = StringField(label='Enter email', validators=[Length(min=7), Email(), DataRequired()])
    r_password = PasswordField(
        label='Enter password', validators=[Length(min=8), DataRequired()])
    r_password_confirm = PasswordField(
        label='Confirm password', validators=[EqualTo('r_password'), DataRequired()])
    r_submit = SubmitField(label='REGISTER')


class WFMHLoginForm(FlaskForm):

    # def validate_r_profile_name(self, new_user):
    #     previously_registered_user = Worker.query.filter_by(
    #         profile_name=new_user.data).first()
    #     if previously_registered_user:
    #         raise ValidationError(
    #             'That username is already registered! Please try again with a different username.')

    # def validate_r_email(self, new_email):
    #     previously_registered_email = Worker.query.filter_by(
    #         worker_email=new_email.data).first()
    #     if previously_registered_email:
    #         raise ValidationError(
    #             'That email is already registered! Please try again with a different email address.')

    l_profile_name = StringField(label='Enter profile name', validators=[DataRequired()])
    l_password = PasswordField(
        label='Enter password', validators=[DataRequired()])
    l_submit = SubmitField(label='LOGIN')

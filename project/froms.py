from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired, Length, ValidationError, InputRequired
import phonenumbers
from project import api_moyklass

times = [('08:00-09:00', '08:00-09:00'), ('09:00-10:00', '09:00-10:00'), ('10:00-11:00', '10:00-11:00'), ('11:00-12:00', '11:00-12:00'),
        ('12:00-13:00', '12:00-13:00'), ('13:00-14:00', '13:00-14:00'), ('14:00-15:00', '14:00-15:00'), ('15:00-16:00', '15:00-16:00'),
        ('16:00-17:00', '16:00-17:00'), ('17:00-18:00', '17:00-18:00'), ('18:00-19:00', '18:00-19:00'), ('19:00-20:00', '19:00-20:00'),
        ('20:00-21:00', '20:00-21:00'),('21:00-22:00', '21:00-22:00'),('22:00-23:00', '22:00-23:00')]

class RegistrationForm(FlaskForm):
    with api_moyklass as api:
        rooms_all = api.get_rooms()
    name = StringField(label=('ФИО'),
                        validators=[DataRequired(message='Обязательное поле.'),
                        Length(min=5, max=80, message='ФИО должен содержать не менее %(min)d и не более %(max)d символов.')])
    phone = StringField(label=('Номер телефона'), validators=[DataRequired(message='Обязательное поле.')])
    audience = SelectField(label=('Футбольное поле'), choices=[(room["id"], room["name"]) for room in rooms_all])
    date = DateField(label=('Дата'), validators=[InputRequired()])
    time = SelectField(label=('Время'), choices=times)
    submit = SubmitField(label=('Отправить заявку'))

    def validate_phone(form, field):
        if len(field.data) > 11:
            raise ValidationError('Неверный формат номера телефона!')
        try:
            input_number = phonenumbers.parse("+7"+field.data)
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Неверный формат номера телефона!')
        except:
            raise ValidationError('Неверный формат номера телефона!')
from project import app
from project.api import time_in_range, datetime_format
from project.froms import RegistrationForm
from project.smtp import send_message_new_lease
from flask import render_template, url_for, redirect, jsonify, flash
from project import api_moyklass

@app.route("/")
def index():
    return redirect(url_for('lease'))

@app.route('/lease', methods=['GET', 'POST'])
def lease():
    form = RegistrationForm()
    if form.validate_on_submit():
        send_message_new_lease(form)
        flash('Спасибо. Заявка принята. В ближайшее время с Вами свяжется наш менеджер.', 'success')
        return redirect('/lease#message') 
    return render_template('lease.html', form=form)


@app.route('/check_free_date/<date>/<time>/<int:audience_value>')
def times(date, time, audience_value):
    current_date = datetime_format(f'{date} {time.split("-")[1]}')
    result = True

    with api_moyklass as api:
        lessons = api.get_lessons(date_from=date, date_to=date)

    for lesson in lessons:
        room_id = lesson['roomId']
        start = datetime_format(f'{lesson["date"]} {lesson["beginTime"]}')
        end = datetime_format(f'{lesson["date"]} {lesson["endTime"]}')

        if time_in_range(start=start, end=end, current_from=current_date, current_to=current_date) and room_id == audience_value:
            result = False
    return jsonify({'result': result})


@app.context_processor
def inject_user():
    return dict(title=app.config['TITLE'])
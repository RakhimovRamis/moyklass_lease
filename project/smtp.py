import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from project import app, api_moyklass

ADDR_FROM = app.config['SMTP_EMAIL']
PASSWORD  = app.config['SMTP_PASSWORD']
PORT = app.config['SMTP_PORT']
SERVER  = app.config['SMTP_SERVER']
SMTP_TO = app.config['SMTP_TO']

def send_message(msg, html):

    msg.attach(MIMEText(html, 'html', 'utf-8'))         
    server = smtplib.SMTP_SSL(SERVER, PORT, timeout=8)
    # server.starttls()                                      
    server.login(ADDR_FROM, PASSWORD)                   
    server.send_message(msg)                          
    server.quit()


def send_message_new_lease(form):           
    msg = MIMEMultipart()                               
    msg['From']    = ADDR_FROM                          
    msg['To']      = SMTP_TO                            
    msg['Subject'] = 'Заявка на аренду футбольного поля'      

    with api_moyklass as api:
        rooms = api.get_rooms()
        audience_name = [room['name'] for room in rooms if room['id'] == int(form.audience.data)][0]

    html = f"""\
    <html>
    <head></head>
    <body>
            <h4>Заявка на аренду футбольного поля</h4>
            <br>
            <p>ФИО: {form.name.data}</p>
            <p>Телефон: {form.phone.data}</p>
            <p>Футбольное поле: {audience_name}</p>
            <p>Дата и время: {form.date.data} {form.time.data}</p>

    </body>
    </html>
    """
    send_message(msg, html)


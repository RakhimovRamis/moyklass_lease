
from flask import Flask
from .api import API

app = Flask(__name__)
app.config.from_object('project.config.Config')
api_moyklass = API(app.config['MOYKLASS_TOKEN'])

import project.views


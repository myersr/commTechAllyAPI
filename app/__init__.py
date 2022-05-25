import logging
from flask import Flask

app = Flask(__name__)

app.logger.setLevel(logging.INFO)
app.logger.info('Elections startup')
from app import routes, errors

from flask import Flask
from src.framework.network import response
from src.currency import bcv

app = Flask(__name__)
PREFIX = '/api/v1'


@app.route(f'{PREFIX}/bcv')
def get_bcv_all():
    return response.success(data=bcv.get_all())

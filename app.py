from flask import Flask
from src.framework.network import response
from src.currency import bcv

app = Flask(__name__)
PREFIX = '/api/v1'


@app.route(f'{PREFIX}/bcv')
def get_bcv_all():
    return response.success(data=bcv.get_all())


@app.route(f'{PREFIX}/bcv/<string:currency>')
def get_currency(currency):
    all_currency = bcv.get_all()
    if currency not in all_currency:
        response.error(
            message=f'Currency {currency} not found', status_code=404)

    return response.success(data={currency: all_currency[currency]})

from bs4 import BeautifulSoup
import requests


def get(url):
    response = requests.get(url, verify=False)
    return BeautifulSoup(response.text, 'html.parser')

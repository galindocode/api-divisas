from src.scraping import html as scraping

BCV_URL = 'https://www.bcv.org.ve/'


def extract_usd(html):
    return html.find('div', {'id': 'dolar'}).find('strong').text


def extract_eur(html):
    return html.find('div', {'id': 'euro'}).find('strong').text


def extract_cny(html):
    return html.find('div', {'id': 'yuan'}).find('strong').text


def extract_try(html):
    return html.find('div', {'id': 'lira'}).find('strong').text


def extract_rub(html):
    return html.find('div', {'id': 'rublo'}).find('strong').text


def get_all():
    html = scraping.get(BCV_URL)
    return {
        "usd": extract_usd(html),
        "eur": extract_eur(html),
        "cyn": extract_cny(html),
        "try": extract_try(html),
        "rub": extract_rub(html),

    }

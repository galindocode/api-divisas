from src.scraping import html as scraping

BCV_URL = 'https://www.bcv.org.ve/'


def extract_currency(html, currency):
    text = html.find('div', {'id': currency}).find('strong').text
    return text.strip()


def get_all():
    html = scraping.get(BCV_URL)
    return {
        "usd": extract_currency(html, 'dolar'),
        "eur": extract_currency(html, 'euro'),
        "cyn": extract_currency(html, 'yuan'),
        "try": extract_currency(html, 'lira'),
        "rub": extract_currency(html, 'rublo'),

    }

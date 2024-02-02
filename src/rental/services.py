import requests
from django.conf import settings
import xml.etree.ElementTree as ET

def address_decoding(lon, lat):
    url = f'https://geocode-maps.yandex.ru/1.x/?apikey={settings.YANDEX_API_KEY}&geocode={lon},{lat}'
    response = requests.get(url)
    
    if response.status_code == 200:
        root = ET.fromstring(response.text)
        geo_object = root.find('.//{http://maps.yandex.ru/ymaps/1.x}GeoObject')
        formatted_text = geo_object.find('.//{http://maps.yandex.ru/address/1.x}formatted').text
        return formatted_text
    else:
        return f"Error: {response.status_code}"

# Example usage

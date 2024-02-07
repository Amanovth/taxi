import requests
from django.conf import settings
import xml.etree.ElementTree as ET

def address_decoding(lon, lat):
    url = f'https://geocode-maps.yandex.ru/1.x/?apikey={settings.YANDEX_API_KEY}&geocode={lon},{lat}'
    response = requests.get(url)
    
    if response.status_code == 200:
        root = ET.fromstring(response.text)
        geo_object = root.find('.//{http://maps.yandex.ru/ymaps/1.x}GeoObject')
        
        # Get the formatted address text
        formatted_text = geo_object.find('.//{http://maps.yandex.ru/address/1.x}formatted').text
        
        # Remove the initial part of the address
        initial_text_to_remove = 'Кыргызстан, Бишкек, '
        formatted_text = formatted_text[len(initial_text_to_remove):]
        
        return formatted_text.title()
    else:
        return f"Error: {response.status_code}"

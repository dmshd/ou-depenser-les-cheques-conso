

import csv
import geopy
import json

from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent = 'dmshd_app')

reverse = RateLimiter(geolocator.reverse, min_delay_seconds = 1, return_value_on_exception = None)


with open("map.json") as f:
    json_data = json.load(f)
    #  for i in json_data:
    #      print(json.dumps(i, indent=2))

with open("magasins-cheques-conso.csv", mode="w") as shops:
    headers = ['id','Appellation','Type de chèque', 'Catégorie','Région', 'Code postal', 'Province', 'Ville','Comté', 'Village', 'Hameau', 'Rue', 'Adresse complète', 'Voir sur Google Maps']
    writer = csv.DictWriter(shops, fieldnames=headers)
    writer.writeheader()
    #  c for company
    for c in json_data:
        print(c['latitude'])
        lat = c['latitude']
        lon = c['longitude']
        location = reverse((lat, lon))
        loc = location.raw
        addr_rich = loc['address']
        full_addr = loc['display_name']
        gmap_link = "https://maps.google.com/?q={},{}".format(c['latitude'], c['longitude']) 
        writer.writerow({
	    'id': c['id'],
            'Appellation': c['name'],
            'Type de chèque': c['type'],
            'Catégorie': c['categories'],
            'Région': addr_rich.get('region', '---'),
            'Code postal': addr_rich.get('postcode', '---'),
            'Province': addr_rich.get('state', '---'),
            'Ville': addr_rich.get('town', '---'),
            'Comté': addr_rich.get('county', '---'),
            'Village': addr_rich.get('village', '---'),
            'Hameau': addr_rich.get('hamlet', '---'),
            'Rue': addr_rich.get('road', '---'),
            'Adresse complète': full_addr,
            'Voir sur Google Maps': "=HYPERLINK(" + gmap_link + ")"
	})


"""
{
  "id": "279559",
  "latitude": "50.7916641",
  "longitude": "5.4554644",
  "name": "KRINGLOOPWINKEL TONGEREN",
  "type": "conso",
  "categories": "Seconde main",
  "distance": "65.26323337701871"
}
"""

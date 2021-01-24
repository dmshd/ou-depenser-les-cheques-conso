

import geopy
import json

from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent = 'dmshd_app')

reverse = RateLimiter(geolocator.reverse, min_delay_seconds = 1, return_value_on_exception = None)

location = reverse((50.6687965, 5.6872244))
print(location.raw)
print(json.dumps(location.raw, indent=2))
elem = location.raw
print(elem['display_name'])
elem_address = elem['address']
print(elem_address["town"])

"""
{  
  "place_id": 118919670,
  "licence": "Data \u00a9 OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
  "osm_type": "way",
  "osm_id": 120839649,
  "lat": "50.66864055",
  "lon": "5.68636053791561",
  "display_name": "12, Route de L\u00e9gipont, Chefneux, Barchon, Blegny, Li\u00e8ge, Wallonie, 4671, Belgi\u00eb / Belgique / Belgien",
  "address": {
    "house_number": "12",
    "road": "Route de L\u00e9gipont",
    "hamlet": "Chefneux",
    "village": "Barchon",
    "town": "Blegny",
    "county": "Li\u00e8ge",
    "state": "Li\u00e8ge",
    "region": "Wallonie",
    "postcode": "4671",
    "country": "Belgi\u00eb / Belgique / Belgien",
    "country_code": "be"
  },
  "boundingbox": [
    "50.668175",
    "50.6691401",
    "5.6855649",
    "5.6871623"
  ]
}

"""

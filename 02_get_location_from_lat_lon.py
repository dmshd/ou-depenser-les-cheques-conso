

import csv
import geopy
import json
import os

from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent = 'dmshd_app')

reverse = RateLimiter(geolocator.reverse, min_delay_seconds = 1, return_value_on_exception = None)

location = reverse((50.6687965, 5.6872244))
print(location.raw)

"""
with open('map.json') as json_f:
    j = json.load(json_f)

pretty_json = json.dumps(j, indent=2)
print(pretty_json)
"""



# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 18:07:22 2020

@author: CEC
"""

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Quito"
dest = "Guayaquil"
key = "rrn3BjOkLhvlMDJXCAC286MaHh8vjnF0"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})

json_data = requests.get(url).json()
print(json_data)
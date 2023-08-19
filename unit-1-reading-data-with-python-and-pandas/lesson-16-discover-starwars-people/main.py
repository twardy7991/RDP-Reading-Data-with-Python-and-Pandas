import numpy as np
import pandas as pd
import requests
import json

http = "https://swapi.co/api/people/?format=json"

data = requests.get(http)

dict = data.json()
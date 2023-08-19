import numpy as np
import pandas as pd
import json


path = r"C:\Users\Patryk\OneDrive\Dokumenty\GitHub\RDP-Reading-Data-with-Python-and-Pandas\unit-1-reading-data-with-python-and-pandas\lesson-10-artists-nested-biography\files\artists.json"
with open(path) as file:
    data  = json.load(file)

artists = pd.json_normalize(data)

biography = pd.json_normalize(
    data,
    record_path = "bio",
    meta = ["name"]
)
biography


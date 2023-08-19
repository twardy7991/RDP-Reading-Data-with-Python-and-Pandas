import numpy as np
import pandas as pd

artists = pd.read_json(
    r"C:\Users\Patryk\OneDrive\Dokumenty\GitHub\RDP-Reading-Data-with-Python-and-Pandas\unit-1-reading-data-with-python-and-pandas\lesson-9-parse-artists-json-file\files\artists.json",
)

artists.drop(columns= ["bio"], inplace= True)

artists.set_index("name", inplace=True)

artists.to_csv("artists.csv")
artists


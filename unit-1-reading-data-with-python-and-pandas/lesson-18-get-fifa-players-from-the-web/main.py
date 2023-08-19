import numpy as np
import pandas as pd
import requests


url = "https://www.fifaindex.com/players/top/fifa20_363/"

data = requests.get(url)

fifa_df = pd.read_html(data.text)

fifa_df = fifa_df[0]

fifa_df = fifa_df.iloc[:, 2:-1]


most_hits_player = fifa_df.sort_values("OVR-POT", ascending=False).head(1)

most_hits_player
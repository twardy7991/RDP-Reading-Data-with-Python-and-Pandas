import numpy as np
import pandas as pd

data_url = 'https://github.com/ine-rmotr-projects/project-files/files/4086772/playstore.xlsx'

df = pd.ExcelFile(data_url)

playstore_df = df.parse("Google_playstore")

content_id_df = df.parse("Content_ID", index_col="Content_ID")

content_id_df

playstore_df

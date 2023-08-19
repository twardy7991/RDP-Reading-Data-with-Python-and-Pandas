import numpy as np
import pandas as pd
import sqlite3

# create a new connection to a db in memory
conn = sqlite3.connect(':memory:')

# create a cursor
c = conn.cursor()

# restore the given van_crime_2003.sql dump
c.executescript(open(r"C:\Users\Patryk\OneDrive\Dokumenty\GitHub\RDP-Reading-Data-with-Python-and-Pandas\unit-1-reading-data-with-python-and-pandas\lesson-13-querying-vancouver-crimes\files\van_crime_2003.sql", 'r').read())

# your code goes here
van_crimes_df = pd.read_sql("""SELECT TYPE,
                            MONTH,
                            DAY,
                            NEIGHBOURHOOD 
                            FROM van_crimes
                            WHERE NEIGHBOURHOOD IN ("Stanley Park" , "West End")
                            """, conn)

crime_types_count = van_crimes_df["TYPE"].value_counts()

crime_types_count
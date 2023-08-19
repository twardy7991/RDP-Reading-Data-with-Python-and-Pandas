import numpy as np
import pandas as pd
import sqlite3

# create a new connection to a db in memory
conn = sqlite3.connect(':memory:')

# create a cursor
c = conn.cursor()

path = r"C:\Users\Patryk\OneDrive\Dokumenty\GitHub\RDP-Reading-Data-with-Python-and-Pandas\unit-1-reading-data-with-python-and-pandas\lesson-14-crypto-currency-database\files\cryptos.sql"
# restore the given cryptos.sql dump
c.executescript(open(path, 'r').read())

# your code goes here
crypto_df = pd.read_sql('''SELECT cryptocoins_cryptocurrency.name AS coin_name, cryptocoins_exchange.name AS exchange, symbol, price_usd, percent_change_7d
                            FROM cryptocoins_cryptocurrency
                            JOIN cryptocoins_exchange
                            ON cryptocoins_cryptocurrency.exchange_id = cryptocoins_exchange.id''', conn)

weekly_change_df = crypto_df.sort_values('percent_change_7d', ascending=False)

weekly_change_df.head(10)
from homework import *
import sqlite3
import pandas as pd
import requests


def test_python():
    assert filter_list([[2, 5, 4, 9], [2, 2], [3, 4, 5]]) == [[3, 4, 5]]
    assert filter_list([[2, 1, 4], [2, 2, 5], [6, 7]]) == [[2, 1, 4], [2, 2, 5]]


def test_sql():
    url = "https://docs.google.com/uc?export=download&id=1BzjCEmvPdi9PZnFGGl7L9N8wSITrrcWf"

    with open('data.db', 'wb') as out_file:
        content = requests.get(url).content
        out_file.write(content)

    con = sqlite3.connect('data.db')  # open a database file

    product_df = pd.read_sql_query(sql_query_1, con)
    customer_df = pd.read_sql_query(sql_query_2, con)

    mask = (customer_df['birth_date'] >= '1990-01-01') & (customer_df['birth_date'] <= '2000-01-01')

    assert set(product_df['quantity_in_stock']) == set([49, 38, 70])
    assert customer_df[mask].shape[0] == customer_df.shape[0]


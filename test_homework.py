from homework import *
from pytest import approx
import numpy as np
import sqlite3
import pandas as pd
import requests
import sklearn


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



def test_model():
    model = train_model()
    features = model.feature_names_in_
    pclass_index = np.where(features == 'PClass')[0][0]
    sex_index = np.where(features == 'SexCode')[0][0]
    age_index = np.where(features == 'Age')[0][0]
    coef = model.coef_[0]

    assert isinstance(model, sklearn.linear_model._logistic.LogisticRegression)
    assert coef[pclass_index] == approx(-1.30651903)
    assert coef[sex_index] == approx(2.33324996)
    assert coef[age_index] == approx(-0.03750101)


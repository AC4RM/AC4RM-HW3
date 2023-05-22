from homework import *
from pytest import approx
from pathlib import Path
from collections import Counter
import numpy as np
import sqlite3
import pandas as pd
import sklearn
import urllib.request
import re


def test_python():
    assert filter_list([[2, 5, 4, 9], [2, 2], [3, 4, 5]]) == [[3, 4, 5]]
    assert filter_list([[2, 1, 4], [2, 2, 5], [6, 7]]) == [[2, 1, 4], [2, 2, 5]]


def test_sql():
    urllib.request.urlretrieve('https://github.com/AC4RM/AC4RM-dataset/blob/main/sql/data.db?raw=true', 'data.db')

    con = sqlite3.connect('data.db')  # open a database file

    product_df = pd.read_sql_query(sql_query_1, con)
    customer_df = pd.read_sql_query(sql_query_2, con)

    mask = (customer_df['birth_date'] >= '1990-01-01') & (customer_df['birth_date'] <= '2000-01-01')

    assert set(product_df['quantity_in_stock']) == set([49, 38, 70])
    assert customer_df[mask].shape[0] == customer_df.shape[0]

    Path('data.db').unlink(missing_ok=True)


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


def test_regex():
    assert '[' in regex_pattern and ']' in regex_pattern
    assert re.search(regex_pattern, 'Afcd')
    assert re.search(regex_pattern, 'xyZa')
    assert not re.search(regex_pattern, 'fig2')


def test_monte_carlo():
    results = []
    np.random.seed(42)
    for i in range(5000):
        result = simple_bettor_v3(10000, 3000, 20)
        results.append(result)

    assert isinstance(results[0], list)
    assert Counter([len(x) for x in results]).most_common(1)[0][0] == 21


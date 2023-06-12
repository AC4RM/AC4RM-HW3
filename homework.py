import numpy as np
import pandas as pd


def filter_list(input_list):
    """
    :param input_list: a nested list
    :return: all the lists whose length is 3 from a nested list
    """
    # Your code here
    pass


# Return products with quantity in stock equal to 49, 38, 70
sql_query_1 = " "

# Return customers born between 1990-01-01 and 2000-01-01
sql_query_2 = " "


def train_model():
    np.random.seed(42)
    titanic = pd.read_csv('https://raw.githubusercontent.com/AC4RM/AC4RM-dataset/main/homework/titanic.csv',
                          index_col=0)
    # Remove the category in the PClass column that only have one observation
    titanic = titanic[titanic.PClass != '*']
    survived = titanic.Survived
    titanic1 = titanic[['PClass', 'SexCode', 'Age']].copy()
    # Find the mean of each PClass and SexCode group
    imputation_dict = titanic1.groupby(['PClass', 'SexCode']).mean().to_dict()
    # Find the index of missing values
    impute_index = titanic1.Age.isnull()
    titanic1.loc[impute_index, 'Age'] = titanic1[impute_index].apply(lambda x: imputation_dict['Age'][(x[0], x[1])], axis=1)
    # Convert 1st, 2nd, 3rd to 1, 2, 3
    titanic1.PClass = titanic1.PClass.map(lambda t: int(t[0]))
    # Your code here


regex_pattern = ' '


def play_round():
    # Roll a 100 sided die.
    # Use the roll_dice function defined above.
    # Return True if win and False if lose.
    # Your code here
    pass


def simple_bettor_v3(initial_funds, initial_wager, intended_rounds):
    # Your code here
    pass

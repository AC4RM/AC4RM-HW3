### Introduction
- This the week 3 homework repository of ERMC K5455 (Applied Coding for Risk Mgmt) at Columbia University. 
- Please refer to Canvas for the homework deadline.

<hr>

### How to submit the homework

1. Define a function `filter_list(input_list)`  using filter to return all the lists whose length is 3 from a nested list. 
   - E.g.: `L = [[2, 5, 4, 9], [2, 2], [3, 4, 5]]` `filter_list(L) => [[3, 4, 5]]`

2. Write the sql query to do the following. You assume that we have the `customers` table from the lecture
   - Return products with quantity in stock equal to 49, 38, 70
   - Return customers born between 1990-01-01 and 2000-01-01

3. We will use the titanic dataset to train a logistic regression model
   - Remove the `Name` column and the category in the `PClass` column that only have one observation
   - Impute the missing values in the `Age` column using the means of the corresponding `PClass` & `SexCode` groups which the samples fall in.
     - You can convert the `groupby` result into a dictionary using `to_dict` method
     - using panda series `apply` method in a lambda function, where the lambda function is defined using the above dictionary
   - The `PClass` column can be treated as an ordinal categorical column. If so, we only need to convert the string values into integer labels
   - Train a logistic regression model using the full dataset and return the model

4. Write a regex pattern that will match any letter in sequence `ABCDEabcde`. You need to use `[]` in the regex pattern. For example
   - `re.search(regex_pattern, 'Afcd')` => Match
   - `re.search(regex_pattern, 'xyZa')` => Match
   - `re.search(regex_pattern, 'fig2')` => Not match
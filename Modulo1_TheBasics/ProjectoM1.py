# Task: Given a csv file and a column name, print the elements in the given column.
#
# Input Format
# First line: filename of a csv file
# Second line: column name

import pandas as pd

filename = input()
column_name = input()

df = pd.read_csv(filename)
arr = df[column_name].values
print(arr)
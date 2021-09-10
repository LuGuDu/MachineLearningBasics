# Building a Logistic Regression model.
#
# Task
# You are given a feature matrix and a single datapoint to predict. Your job will be to
# build a Logistic Regression model with the feature matrix and make a prediction (1 or 0)
# of the single datapoint.
#
# Input Format
# First line: Number of data points in the feature matrix (n)
# Next n lines: Values of the row in the feature matrix, separated by spaces
# Next line: Target values separated by spaces
# Final line: Values (separated by spaces) of a single datapoint without a target value

from sklearn.linear_model import LogisticRegression

n = int(input())
X = []
for i in range(n):
    X.append([float(x) for x in input().split()])
y = [int(x) for x in input().split()]
datapoint = [float(x) for x in input().split()]

model = LogisticRegression()
model.fit(X, y)
print(model.predict([datapoint])[0])
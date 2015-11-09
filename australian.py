#!/usr/bin/env python
#title          :australian.py
#description    :A classification task to show how to improve SVMs
#author         :Henry Lin
#version        :0.0.1
#python_version :2.7.6
#================================================================================

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.grid_search import GridSearchCV

dataset = pd.read_csv("data/australian.data", header=None, sep=" ")
X = dataset.drop(14, axis=1)        # Features
y = dataset[14]                     # Labels

# Produces a "one hot encoding" of the data
scaler = StandardScaler()
X = scaler.fit_transform(X)
conv_X = pd.get_dummies(pd.DataFrame(X), columns=[0, 3, 4, 5, 7, 8, 10, 11])

X_train, X_test, y_train, y_test = train_test_split(conv_X, y, test_size=0.25,
                                                    random_state=888)

svm_parameters = {"C": [0.5, 1, 2, 3, 4, 10], "kernel": ["rbf", "poly", "linear"]}
models = [LogisticRegression, GridSearchCV]
model_parameters = [[], [SVC(), svm_parameters]]
for model, model_parameters in zip(models, model_parameters):
    clf = model(*model_parameters)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)
    print "Accuracy score for {0}: {1}" \
            .format(model.__name__, accuracy_score(y_test, predictions))

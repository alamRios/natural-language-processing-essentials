# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 14:40:31 2019

@author: Turing
"""

from sklearn.feature_extraction.text import CountVectorizer
from _pickle import load

# Cargar datos
y = []
inputt = open('dim-y_list.pk1','rb')
y = load(inputt)
inputt.close()

reviews_content = []
inputt = open('dim-x_list.pk1','rb')
reviews_content = load(inputt)
inputt.close()

# Vectorizar corpus
vectorizer = CountVectorizer(min_df=1, ngram_range=(1,1))
features = vectorizer.fit_transform(reviews_content)
X = features
# Procesamiento
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
        X,y, test_size = 0.3)

from sklearn.naive_bayes import MultinomialNB

clf = MultinomialNB()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

from sklearn import metrics

print(">>>>>>>> MultinomialNB")
print(">> accuracy of prediction is:", clf.score(X_test, y_test))
print(">> confusion matrix:\n ", metrics.confusion_matrix(y_test, y_pred))
print(">> classification report:\n", metrics.classification_report(y_test, y_pred))
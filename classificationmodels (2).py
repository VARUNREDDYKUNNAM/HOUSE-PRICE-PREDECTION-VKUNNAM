# -*- coding: utf-8 -*-
"""classificationmodels.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pY0g0ae4rGDcSIAAuC2WS6NMoSjt4O-V
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

data = pd.read_csv('/content/NY-House-Dataset.csv')

median_price = data['PRICE'].median()
print(f"Median Price: {median_price}")

data['Price_Category'] = (data['PRICE'] >= median_price).astype(int)

X = data.drop(['PRICE', 'Price_Category'], axis=1)
y = data['Price_Category']

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

categorical_cols = X.select_dtypes(include=['object']).columns
numerical_cols = X.select_dtypes(include=['number']).columns
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ])

X_preprocessed = preprocessor.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_preprocessed, y, test_size=0.2, random_state=42)
classifier = RandomForestClassifier(n_estimators=100, random_state=42)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(classification_report(y_test, y_pred))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
data = pd.read_csv('/content/NY-House-Dataset.csv')
median_price = data['PRICE'].median()
data['Price_Category'] = (data['PRICE'] >= median_price).astype(int)
X = data.drop(['PRICE', 'Price_Category'], axis=1)
y = data['Price_Category']

categorical_cols = X.select_dtypes(include=['object']).columns
numerical_cols = X.select_dtypes(include=['number']).columns

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ])

X_preprocessed = preprocessor.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_preprocessed, y, test_size=0.2, random_state=42)
classifier = DecisionTreeClassifier(random_state=42)
classifier.fit(X_train, y_train)
y_pred3 = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(classification_report(y_test, y_pred))

from sklearn.metrics import confusion_matrix
forest_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
forest_classifier.fit(X_train, y_train)
forest_predictions = forest_classifier.predict(X_test)
tree_classifier = DecisionTreeClassifier(random_state=42)
tree_classifier.fit(X_train, y_train)
tree_predictions = tree_classifier.predict(X_test)
forest_cm = confusion_matrix(y_test, forest_predictions)
tree_cm = confusion_matrix(y_test, tree_predictions)

import matplotlib.pyplot as plt
import seaborn as sns
def plot_confusion_matrix(cm, title):
    plt.figure(figsize=(6,5))
    sns.heatmap(cm, annot=True, fmt="d", cmap='Blues')
    plt.title(f'Confusion Matrix for {title}')
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.show()
plot_confusion_matrix(forest_cm, 'Random Forest Classifier') # From confusion matrix, ModelAccuracy = (417+434)/(417+434+55+55)≈0.9406 (or 94.06%)
plot_confusion_matrix(tree_cm, 'Decision Tree Classifier')   # From confusion matrix, ModelAccuracy = (416+414) / (416+414+73+58)=0.9149 (OR 91.49%) => Random Forest is the best out of these two and Decision Tree is the worst
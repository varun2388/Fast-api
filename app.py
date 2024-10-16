import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load and preprocess the dataset
@st.cache
def load_data():
    data = pd.read_csv('data.csv')
    data.fillna(0, inplace=True)
    return data

data = load_data()

# Split the data into training and testing sets
X = data.drop('target', axis=1)
y = data['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple ML model using scikit-learn
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Create a Streamlit app to display the model and predictions
st.title('Simple ML Model with Streamlit')
st.write('Accuracy:', accuracy)

st.write('Predictions:')
st.write(y_pred)

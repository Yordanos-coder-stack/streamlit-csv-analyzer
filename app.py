import streamlit as st
from PIL import Image

st.title("My First Streamlit App")
st.write("Hello! I am learning Streamlit ")

name = st.text_input("Enter your name")

if name:
    st.success(f"Welcome {name}!")
# Button
if st.button("click me"):
    st.write("You clicked the button!")



import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

st.title("Simple Price Prediction App")

# Training data
x = np.array([1,2,3,4,5]).reshape(-1,1)
y = np.array([10,20,30,40,50])

model = LinearRegression()
model.fit(x,y)

user_input = st.number_input("Enter a value:")

if st.button("Predict"):
    result = model.predict([[user_input]])
    st.success(f"Predicted value is: {result[0]}")
import streamlit as st
import pandas as pd

st.title("CSV Analyzer")

file = st.file_uploader("Upload CSV", type="csv")

if file:
    df = pd.read_csv(file)
    st.dataframe(df)
    st.write("Summary:")
    st.write(df.describe())
    st.bar_chart(df.select_dtypes(include="number"))

import streamlit as st
import pandas as pd

st.title("Streamlit Widgets")

# Input
name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello, {name}!")

# Slider
age = st.slider("Select your age:", 0, 150, 25)

# Dropdown
options = ["Python", "JavaScript", "C++", "Java"]
choice = st.selectbox("Select your favorite programming language:", options)
st.write(f"You selected: {choice}")

# Table
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
st.write("Here is the table:")
df.to_csv("sampled.csv")
st.dataframe(df)

# File Operation
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
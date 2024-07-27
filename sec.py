# Function to add two numbers
import streamlit as st
from streamlit_chat import message
def add_numbers(a, b):
    return a + b

# Numbers to be added
num1 = 2
num2 = 3

# Adding the numbers
result = add_numbers(num1, num2)

# Printing the result
st.write(f"The sum of {num1} and {num2} is {result}")
print(f"The sum of {num1} and {num2} is {result}")
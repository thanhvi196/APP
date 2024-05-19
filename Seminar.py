import streamlit as st
import pandas as pd
import numpy as np
st.title('XIN CHAO CAC BAN')
col1, col2, col3 = st.columns(3)

credit_score = col1.number_input('Credit Score', min_value=df['CreditScore'].min(), max_value=df['CreditScore'].max())
geography = col2.selectbox('Geography', df['Geography'].unique())
gender = col3.selectbox('Gender', df['Gender'].unique())

age = st.number_input('Age', min_value=df['Age'].min(), max_value=df['Age'].max())
tenure = st.number_input('Tenure (Years with Bank)')
balance = st.number_input('Balance (USD)')
num_products = st.number_input('Number of Products')

has_credit_card = st.checkbox('Has Credit Card?')
is_active_member = st.checkbox('Is Active Member?')
estimated_salary = st.number_input('Estimated Salary (USD)')

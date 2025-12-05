import streamlit as st
import pandas as pd
import numpy as np
 
st.title("📈 Simple Line Chart")
st.title("this is line chart using streamlit")
data = pd.DataFrame({
    'x': np.arange(1, 11),
    'y': np.random.randint(20, 100, 10)
})
 
st.line_chart(data, x='x', y='y')
 
st.title("My First Streamlit App")
st.write("Hello! Streamlit is working.")
 
 
st.title("My First Streamlit App")
st.write("Hello! Streamlit is working.")


import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
import pygwalker as pyg

st.header('st.write')

# Example 1

st.write('Hello, *World :Sunglasses')

# Example 2

st.write(1234)

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

# example 3

st.write(df)

# example 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

pyg.walk(df, env='Streamlit')

# example 5.

df2 = pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])

c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', tooltip=['a', 'b', 'c'])
st.write(c)

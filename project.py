import streamlit as st
import pandas as pd
import io

#load csv
df=pd.read_csv("startup_funding.csv")

#clean column names
df.columns = df.columns.str.strip()

#show dataframes
st.dataframe(df)


#proper df.info() display


"""
io.stringIO():
IT BEHAVES LIKE A FILE
 but it lives in ram,not in disk
 you can write a text to it and read text from it
"""

st.write("###Dtaset Info")
buffer = io.StringIO()
df.info(buf=buffer)
st.text(buffer.getvalue())

#check column names
st.write("###columns available")
st.write(df.columns.tolist())


#fix column name based on actual csv
if 'Investors Name' in df.columns:
    df['Investors Name'] = df['Investors Name'].fillna('Undisclosed')
    investors=sorted(df['Investors Name'].unique().tolist())
    st.write("###Distinct Investors Names")
    st.write(investors)
else:
    st.error("Column 'Investors Name' not found. check column list above.")
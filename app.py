import sqlite3
import pandas as pd
import streamlit as st
st.set_page_config(layout="wide")
conn=sqlite3.connect("products.db")
df=pd.read_sql("select * from products",conn)
cols=st.columns(4)
for i,row in df.iterrows():
    with cols[i%4]:
        st.image(row["image"])
        st.write(row["name"])
        st.write(row["price"])
        st.link_button("View",row["link"])
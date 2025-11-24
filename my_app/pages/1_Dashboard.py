import streamlit as st
import pandas as pd
import sqlite3
import os

st.set_page_config(page_title="Dashboard")

# the path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))   # -> my_app/
DB_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "DATA", "intelligence_platform.db"))

# loading my tables in intelligence_platform.db here

def load_table(table_name):
    try:
        conn = sqlite3.connect(DB_PATH)
        #reads the table and stores it in a DataFrame. Without it, the function won’t return the table’s data.
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        conn.close()
        return df

    except :
        st.error(f"Error reading {table_name}")
        return None

st.title("Intelligence Platform Dashboard")
st.write("Below you are gonna see the 4 databases tables stored in intelligence_platform.db.")

# users table
st.subheader("Users table")
st.dataframe(load_table("users"))

# cyber_incidents table
st.subheader("Cyber Incidents table")
st.dataframe(load_table("cyber_incidents"))

# dataset_metadata table
st.subheader("Dataset table ")
st.dataframe(load_table("datasets"))

# it_tickets table
st.subheader("IT Tickets table ")
st.dataframe(load_table("tickets"))

# Logout button
st.divider()
if st.button("Log out"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.info("You have been logged out.")
    st.switch_page("login.py")

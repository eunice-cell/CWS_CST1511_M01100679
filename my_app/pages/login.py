import streamlit as st
from pathlib import Path
import bcrypt

USER_FILE = "DATA/users.txt"

st.set_page_config(page_title="Login")

st.markdown("""
<style>
.stApp { background-color: #5C4033; color: #FFFDD0; }
</style>
""", unsafe_allow_html=True)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# Load users from users.txt so those only these can log in
def load_users():
    users = {}
    if Path(USER_FILE).exists():
        with open(USER_FILE, "r") as file:
            for line in file:
                username, hash_pw = line.strip().split(",")
                users[username] = hash_pw
    return users

# authenticate the user
def authenticate_user(username, password):
    users = load_users()

    if username in users:
        # Get the stored hashed password for this username and convert it to bytes
        stored_hash = users[username].encode("utf-8")
        # Check if the entered password matches the stored hashed password
        if bcrypt.checkpw(password.encode("utf-8"), stored_hash):
            st.session_state.logged_in = True
            st.success(f"Welcome {username}!")
            st.switch_page("1_Dashboard")
            return

    st.error("Invalid username or password.")
    st.session_state.logged_in = False



st.title("Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    authenticate_user(username, password)

with st.expander("See details"):
    st.write("Login using username + hashed password stored in DATA/users.txt.")

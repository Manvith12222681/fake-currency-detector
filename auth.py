import streamlit as st

users = {}

def login():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and users[username] == password:
            st.session_state["logged_in"] = True
            st.session_state["user"] = username
            st.success("Login successful")
        else:
            st.error("Invalid credentials")

def signup():
    username = st.text_input("New Username")
    password = st.text_input("New Password", type="password")

    if st.button("Sign Up"):
        users[username] = password
        st.success("Account created")

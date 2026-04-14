import streamlit as st

# Simple in-memory user storage
users = {}

def signup():
    st.subheader("Create Account")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        if username in users:
            st.error("User already exists")
        else:
            users[username] = password
            st.success("Account created successfully")

def login():
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and users[username] == password:
            st.session_state["logged_in"] = True
            st.session_state["user"] = username
            st.success("Login successful")
        else:
            st.error("Invalid credentials")
import streamlit as st

# Hardcoded user credentials for demonstration purposes
USERNAME = "user"
PASSWORD = "password"

# Function to verify credentials
def check_credentials(username, password):
    return username == USERNAME and password == PASSWORD

# Initialize session state for authentication status
if 'authentication_status' not in st.session_state:
    st.session_state.authentication_status = None

def login():
    st.title("Login Page")

    # Input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Login button
    if st.button("Login"):
        if check_credentials(username, password):
            st.session_state.authentication_status = True
            st.experimental_rerun()  # Rerun the app to reflect the authentication status
        else:
            st.session_state.authentication_status = False
            st.error("Username/password is incorrect")

def main():
    # Check the authentication status
    if st.session_state.authentication_status:
        with open('Dashboard.py') as file:
            exec(file.read())
    else:
        login()

if __name__ == "__main__":
    main()

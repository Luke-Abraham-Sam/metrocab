import streamlit as st

st.title("Login Page")

# Initialize session state for login status if it doesn't exist
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# If not logged in, show the login form
if not st.session_state.logged_in:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Sign In"):
        # Fixed the typo here
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
            st.success("Logged in successfully!")
            st.balloons()
            st.rerun()  # Rerun the app to refresh the view
        else:
            st.error("Invalid username or password.")

# If logged in, show the secure content
else:
    st.write("### Welcome to the Dashboard!")
    st.write("This is secure content only visible after logging in.")
    
    if st.button("Log Out"):
        st.session_state.logged_in = False
        st.rerun()
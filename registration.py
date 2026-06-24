import streamlit as st

st.title("Student Registration")

# Input fields
name = st.text_input("Full Name")
email = st.text_input("Email")
mobile = st.text_input("Mobile Number")

# Fixed: Changed st.selection to st.selectbox
course = st.selectbox(
    "Select Course", 
    ["Python", "Java", "AI/ML"]
)

# Added a submit button to process the registration
if st.button("Register"):
    if name and email and mobile:
        st.success(f"Successfully registered {name} for the {course} course!")
    else:
        st.warning("Please fill out all the fields before submitting.")
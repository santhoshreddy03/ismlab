import streamlit as st
from PIL import Image

# Set the page title
st.set_page_config(page_title="Login Page")

# Define the login function
def login(username, password):
    if username == "san" and password == "pwd123":
        st.success("Login successful!")
    else:
        st.error("Invalid username or password.")

# Load the image
image = Image.open("logo.png")  # Replace "logo.png" with your image file name

# Create a column layout
col1, col2 = st.columns(2)

# Display the image in the first column
with col1:
    st.image(image, width=200)

# Display the login form in the second column
with col2:
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Add a login button
    if st.button("Login"):
        login(username, password)

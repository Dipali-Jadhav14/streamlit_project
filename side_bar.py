import streamlit as st
#code for generate login form
email=st.text_input("enter your email")
password=st.text_input("enter your password")
btn=st.button("login")
if btn:
    if email=='yashaswi@gmail.com' and password=='1234':
        st.success('Login Successful')


#code for generae ballons
        st.balloons()
    else:
        st.error('Login Failed')

#code for generate sidebar
st.sidebar.write("hello this is my side bar")
import streamlit as st
st.title(" hello streamlit !!!")
st.header("hi")
st.subheader("i am dipa")
st.text("hi' dipali")
st.markdown("hi rekha")
st.markdown("google('https://www.google.com")
st.caption("hii i am caption ")

json={"a":"1,2,3","b":"4,5,6"}
st.json(json)


code="""
print("hello world")
def fun():"""

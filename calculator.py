#streamlit run filename.py

import streamlit as st

st.title("Simple Calculator")
st.markdown("Welcome to my first Web App!")

c1,c2= st.columns(2)
fnum= c1.number_input("Enter first number",value=0)
snum= c2.number_input("Enter second number",value=0)

operation = ["Add","Subtract","Multiply","Dvision"]
choice= st.radio("Select Operation ", operation)

button=st.button("Caluclate")

result=0

if button:
    if choice=="Add":
         result=fnum+snum
    if choice=="Subtract":
         result=fnum-snum
    if choice=="Multiply":
         result=fnum*snum
    if choice=="Divide":
         result=fnum/snum

st.success(f"Result: {result}")
st.balloons()              



                 

   
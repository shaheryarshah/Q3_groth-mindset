#import depencies
import streamlit as st

st.set_page_config("Growth Mindset Application project_icon=🌹")
st.title("GrowthMindset Project")
st.header("Welcome to your GrowthMindset Journey")
st.write("Welcome")

#quote section
st.write("Write cuote")
st.header("Welcome to")
user_input = st.text("Write your chalanges")

#condition

if user_input:
    st.success(f"you are facing: {user_input}. keep pushing")
else:
    st.warning("tell us about your chalenges")

    #reflecxing
    
  
    st.header("Reflect on your learning")
    refletion = st.text_area("write your reflection here")

    if refletion:
        st.success(f"Great!")
    else:
        st.info("please write your reflection")


    #achivement
        
    st.header("celebrate")
    achivement = st.text_input("share something")

    if achivement:
        st.success(f"you are achieving: {achivement}")
    else:
        st.info("please share your all achivement")

    #footer
        
    st.write("Thank you for your participation")
    st.write("Created by: Muhammad Shaheryar")
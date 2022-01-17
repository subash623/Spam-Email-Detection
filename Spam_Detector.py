import pickle
import streamlit as st
from win32com.client import Dispatch

def speak(text):
   speak=Dispatch(("SAPI.SpVoice"))
   speak.Speak(text)

model=pickle.load(open("spam.pkl","rb"))
cv=pickle.load(open("vectorizer.pkl","rb"))

def main():
   st.title("Welcome to Email Spam Detector")
   st.subheader("Type a message below")
   msg=st.text_input("Enter a Text: ")
   if st.button("Predict"):
       df=[msg]
       vect=cv.transform(df).toarray()
       prediction=model.predict(vect)
       result=prediction[0]
       if result==1:
           st.error("Sorry !This Mail is Spam Try another mail")
           speak("Sorry !This Mail is Spam Try another mail")
       else:
           st.success("Congratulation!! This mail is not Spam")
           speak("Congralutation!! This mail is not Spam")
main()
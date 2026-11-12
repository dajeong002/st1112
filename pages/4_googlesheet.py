import streamlit as st
import pandas as pd

st.title("구글 시트 연동")


url = "https://docs.google.com/spreadsheets/d/1KQHpA7ZgvOIfMYyxEpi0QXddYb3-Kwx4NPNwUZQjB6Y/export?format=csv&gid=0"
data = pd.read_csv(url)
# st.dataframe(data)

# 문항 1,2,3 만들기
question1 = data.iloc[0, 1]
question2 = data.iloc[1, 1]
question3 = data.iloc[2, 1]

st.write(question1)
answer1 = st.text_input("문항 1 답변")
st.write(question2)
answer2 = st.text_input("문항 2 답변")
st.write(question3)
answer3 = st.text_input("문항 3 답변")
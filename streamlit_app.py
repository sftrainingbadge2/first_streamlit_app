import streamlit

streamlit.title('My Parents new healthy diner')

streamlit.header('Breakfast Menu')

streamlit.text('Omega3 & Blueberry Oat Meal')

streamlit.text('Idli & Sambhar')

streamlit.text('Pongal')

streamlit.title('My MoMs new healthy diner')

streamlit.header('Breakfast Favourites')

streamlit.text('Poori and Potato curry')

streamlit.text('Idli & Sambhar')

streamlit.text('Chappathi and chenna')

streamlit.title('Build your own smoothie')
import pandas
myfruitlist = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(myfruitlist)

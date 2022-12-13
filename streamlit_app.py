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
myfruitlist = myfruitlist.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(myfruitlist.index)

# Display the table on the page.
streamlit.dataframe(myfruitlist)

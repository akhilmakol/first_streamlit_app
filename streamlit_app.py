
# Github and Streamlit Set-up 

import streamlit
streamlit.title('My Mom New Healthy Diner')

# Github and Streamlit Iterative Improvements 

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 mega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Importing Pandas & Fetching the datafram from AWS S3 Bucket 

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# We want to filter the table data based on the fruits a customer will choose, so we'll pre-populate the list to set an example for the customer.
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])

# Display the table on the page.
streamlit.dataframe(my_fruit_list)




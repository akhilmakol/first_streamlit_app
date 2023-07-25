
# Github and Streamlit Set-up 
import streamlit
import pandas
import requests
import snowflake.connector 
from urllib.error import URLError


streamlit.title('My Mom New Healthy Diner')

# Github and Streamlit Iterative Improvements 
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Importing Pandas & Fetching the datafram from AWS S3 Bucket 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# We want to filter the table data based on the fruits a customer will choose, so we'll pre-populate the list to set an example for the customer.
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])

# Display the table on the page.
# streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)

# creat the repeatable code block (called d function)
def get_fruityvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   return fruityvice_normalized

# New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
    streamlit.write('The user entered ', fruit_choice)
except URLError as e:
  streamlit.error()

# don't run anything past here while we troubleshoot
streamlit.stop()

streamlit.header("The fruit load list contains:")
#Snowflake-related functions
def getfruit_load_list():
   with my_cur.cursor() as my_cur:
      my_cur.execute("select * from fruit_load_list")
      my_cur.fetchall()
 # Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = getfruit_load_list
   sreamlit.dataframe(my_data_rows)
   
fruit_choice1 = streamlit.text_input('What fruit would you like information about?','Banana')
add_my_fruit= requests.get("https://fruityvice.com/api/fruit/" + fruit_choice1)
streamlit.write('Thanks for adding ', add_my_fruit)
fruityvice_normalized1 = pandas.json_normalize(add_my_fruit.json())
streamlit.dataframe(fruityvice_normalized1)
my_cur.execute("insert into fruit_load_list values ('from streamlit')")

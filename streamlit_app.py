
import streamlit

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# let's create checklist to allow customers to multiselect fruits to create their own smoothy
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# display the fruit table on page
streamlit.dataframe(fruits_to_show)

#new section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruit you would like information about?', 'apple')
streamlit.write('The User entered', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

#take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# output the normalized reponse on the screen as a table
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

#query our trail account data

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)

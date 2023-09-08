import streamlit
import pandas as pd

streamlit.title("My parents new healthy dinner")

streamlit.header("Breakfast Menu")

streamlit.text("🥣 - Omega 3 and Blueberry Oatmeal")
streamlit.text("🥗 - Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 - Hard-Boiled Free-Range Egg")
streamlit.text("🥑🍞 - Advocado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

My_Fruit_List = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(My_Fruit_List)

My_Fruit_List = My_Fruit_List.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
Fruits_Selected = streamlit.multiselect("Pick some fruits:", list(My_Fruit_List.index), ['Avocado', 'Strawberries', 'Apple'])
Fruits_To_Show = My_Fruit_List.loc(Fruits_Selected)

# Display the table on the page.
streamlit.dataframe(Fruits_To_Show)



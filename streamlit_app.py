import streamlit as st
import snowflake.connector

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(),
CURRENT_REGION()")
my_data_row = my_cur.fetchone()
st.text("Hello from Snowflake:")
st.text(my_data_row)

#st.header with "Zena's Amazing Athleisure Catalog"
#Pick a sweatsuit solor or style:
#st. single pick Color/Style
#render image from URL
#Our warm, comfortable, {f Yellow sweatsuit}!
#Price: 65.00
#Sizes Available: Child L | Child M | Child S ..... Women's XXL
#
#Consider white/grey/black
#OR
#BONUS: 1:Yellow Headband & 2 Pink Wristbands

import streamlit as st
import snowflake.connector
import pandas as pd

# #initial test
# my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# st.text("Hello from Snowflake:")
# st.text(my_data_row)


    #st.header with "Zena's Amazing Athleisure Catalog"
streamlit.title('Zena\'s Amazing Athleisure Catalog')

    #Pick a sweatsuit color or style:
# connect to snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
# run a snowflake query and put it all in a var called my_catalog
my_cur.execute("select color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()
# put the dafta into a dataframe
df = pd.DataFrame(my_catalog)
# temp write the dataframe to the page so I Can see what I am working with
st.text('write the dataframe to the page so I Can see what I am working with')
st.write(df)
# put the first column into a list
color_list = df[0].values.tolist()
st.text(print(color_list))

    #st. single pick Color/Style
# Let's put a pick list here so they can pick the color
option = st.selectbox('Pick a sweatsuit color or style:', list(color_list))


    #render image from URL
# We'll build the image caption now, since we can
product_caption = 'Our warm, comfortable, ' + option + ' sweatsuit!'
# use the option selected to go back and get all the info from the database
my_cur.execute("select direct_url, price, size_list, upsell_product_desc from catalog_for_website where color_or_style = '" + option + "';")
df2 = my_cur.fetchone()
streamlit.image(
df2[0],
width=400,
    #Our warm, comfortable, {f Yellow sweatsuit}!
caption= product_caption
)

    #Price: 65.00
streamlit.write('Price: ', df2[1])

    #Sizes Available: Child L | Child M | Child S ..... Women's XXL
streamlit.write('Sizes Available: ',df2[2])

#Consider white/grey/black
#OR
#BONUS: 1:Yellow Headband & 2 Pink Wristbands
streamlit.write(df2[3])


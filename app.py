import pandas as pd 
import pickle as pk 
import streamlit as st 

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://img.freepik.com/free-photo/observation-urban-building-business-steel_1127-2397.jpg");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
[data-testid="stToolbar"] {
    right: 2rem;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

model =pk.load(open('E:\ml project\house price prediciton\house_price_pridiction.pk1','rb'))

st.header('HOUSE PRICE PREDICITOR')

data=pd.read_csv('E:\ml project\house price prediciton\cleaned_data.csv')

loc=st.selectbox('choose the location ',data['location'].unique())

sqft=st.number_input('enter total sqft')
beds=st.number_input('enter no of bedrooms')
bath=st.number_input('enter no of bathrooms')

balc=st.number_input('enter no of balconies')


input =pd.DataFrame([[loc,sqft,bath,balc,beds]],columns=['location','total_sqft','bath','balcony','bedroom'])

if st.button ('predict price'):
    output=model.predict(input)

    out_str='price of the house is rs '+ str(round(output[0]*100000,2))
    st.success(out_str)
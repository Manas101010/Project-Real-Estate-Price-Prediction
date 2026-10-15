
import pickle
import numpy as np
import pandas as pd
import streamlit as st
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

df = pd.read_csv(BASE_DIR / "Final_Project.csv")

with open(BASE_DIR / "regression_model.pkl", "rb") as pickle_in:
    reg = pickle.load(pickle_in)


def predict_price(Area_SqFt,Floor_No,Bedroom):
    x = np.zeros(7)
    
    x[0] = Area_SqFt
    x[1] = Floor_No
    x[2] = Bedroom

    return reg.predict([x])[0]

def run_ml_app():
    st.subheader('Please enter the required details :')
    Location = st.selectbox('Select the Location',(df['Region'].sort_values().unique()))
    Area_SqFt = st.slider("Select Total Area in SqFt",500,int(max(df['Area_SqFt'])),step=100)    
    Floor_No = st.selectbox("Enter Floor Number",(df['Floor_No'].sort_values().unique()))
    Bathroom = st.selectbox("Enter Number of Bathroom",(df['Bathroom'].sort_values().unique()))
    Bedroom = st.selectbox("Enter Number of Bedroom",(df['Bedroom'].sort_values().unique()))
    Property_Age = st.selectbox('Select the Property Age',(df['Property_Age'].sort_values().unique()))
    result= ""
  
    if st.button("Calculate Price"):
        result = predict_price(Area_SqFt,Floor_No,Bedroom)
    st.success('Total Price in Lakhs : {}'.format(result))
    
if __name__=='__main__':
    run_ml_app()

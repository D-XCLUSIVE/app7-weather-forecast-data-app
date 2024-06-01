# 285 ploting data dynamically

import streamlit as st 
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selector, and subheader
st.title("Weather Forcast For the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forcast Days", min_value=1, max_value=5, help='Select the number of the forcasted days')

option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place} ")


if place: 
    try:
        filtered_data = get_data(place, days)
        

        if option == "Temperature":
            temperature =[ dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]

            figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"CLear": "images/clear.png", "Clouds":"images/cloud.png", "Rain":"images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)
    except:
        print("That place does not exist")


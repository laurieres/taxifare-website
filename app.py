import streamlit as st
import requests
from datetime import datetime, date, time
from geopy.geocoders import Nominatim

import numpy as np
import pandas as pd

st.markdown("""# Welcome to TaxiFare Website 🚕
## Sponsored by *@lewagon* 🚀""")


## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# Idées:
# Rentrer une adresse plutot que des locs

def geocode_address(address):
    geolocator = Nominatim(user_agent="geoapi")
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        st.error(f"Could not geocode the address: {address}")
        return None, None

pickup_date = st.date_input('When do you want to go fot a ride ?')
pickup_time = st.time_input('At what time ?')
pickup_datetime = datetime.combine(pickup_date, pickup_time)
st.write('The current date & time are ', pickup_datetime)

# Input field for pickup address with suggestions
pickup_address = st.text_input('Where do you want to be picked up? (Address)', key="pickup_address")
pickup_suggestions = st.empty()

# Update suggestions based on user input
if pickup_address:
    pickup_suggestions_list = geocode_address(pickup_address)
    pickup_suggestions.selectbox("Choose from suggestions:", pickup_suggestions_list)

pickup_latitude, pickup_longitude = geocode_address(pickup_address) if pickup_address else (None, None)
st.write('The pickup loc is ', pickup_latitude, pickup_longitude)

# Input field for dropoff address with suggestions
dropoff_address = st.text_input('Where do you want to be dropped off? (Address)', key="dropoff_address")
dropoff_suggestions = st.empty()

# Update suggestions based on user input
if dropoff_address:
    dropoff_suggestions_list = geocode_address(dropoff_address)
    dropoff_suggestions.selectbox("Choose from suggestions:", dropoff_suggestions_list)

dropoff_latitude, dropoff_longitude = geocode_address(dropoff_address) if dropoff_address else (None, None)
st.write('Your arrival loc is ', dropoff_latitude, dropoff_longitude)

passenger_count_input = st.number_input('Number of people')
passenger_count = int(passenger_count_input)
st.write('Fare for', round(passenger_count), 'people')

# 1. Calling the URL

url = 'https://taxifare.lewagon.ai/predict'

#if url == 'https://taxifare.lewagon.ai/predict':

    #st.markdown()


# 2. Let's build a dictionary containing the parameters for our API...

params = {'pickup_datetime': pickup_datetime,
          'pickup_longitude': pickup_longitude,
          'pickup_latitude': pickup_latitude,
          'dropoff_longitude': dropoff_longitude,
          'dropoff_latitude': dropoff_latitude,
          'passenger_count': passenger_count}

#3. Let's call our API using the `requests` package...

response = requests.get(url=url, params=params)

#4. Let's retrieve the prediction from the **JSON** returned by the API...

print(response.json())

if response.status_code == 200:
    st.markdown(f"# Your estimated fare is {round(response.json()['fare'],2)} $ 💸")
else:
    st.write(f"Erreur {response.status_code}: {response.text}")

st.markdown(f"Try & Update")



## Finally, we can display the prediction to the user

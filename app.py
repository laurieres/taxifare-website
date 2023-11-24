import streamlit as st
import requests
from datetime import datetime, date, time

import numpy as np
import pandas as pd

st.markdown("""# Welcome to TaxiFare Website 🚕
## Sponsored by *@lewagon* 🚀""")


## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

pickup_date = st.date_input('When do you want to go fot a ride ?')
pickup_time = st.time_input('At what time ?')
pickup_datetime = datetime.combine(pickup_date, pickup_time)
st.write('The current date & time are ', pickup_datetime)

pickup_longitude = st.number_input('Where do you want to be picked up (longitude) ?')
pickup_latitude = st.number_input('Where do you want to be picked up (latitude) ?')
st.write('The pickup loc is ', pickup_longitude, pickup_latitude)

dropoff_longitude = st.number_input('Where do you want to be droped off (longitude) ?')
dropoff_latitude = st.number_input('Where do you want to be droped off (latitude) ?')
st.write('Your arrival loc is ', dropoff_longitude, dropoff_latitude)

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

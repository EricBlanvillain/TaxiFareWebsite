import streamlit as st
import requests


st.sidebar.markdown(f"""
    # Documentation:
    """)

st.sidebar.text("Try this app to predict TaxiFare in NY")



'''
# TaxiFareModel:
## Date & Time:
'''

import datetime

d = st.date_input("insert pick up date:",
                  datetime.date(2019, 7, 6))
st.write('pick up date is:', d)

t = st.time_input('insert pick up time:',
                  datetime.time(8, 45))
st.write('pick up time is:', t)

'''
## Location:
'''

#$ curl -X POST 'https://places-dsn.algolia.net/1/places/query' \
#  --data '{"query": "Paris", "type": "city", "countries": ["us", "fr"]}'

def fetch_pickup_location(pickup_location):
    """
    Get the location from latitude and longitude
    """
    params = {
        'pickup_location': pickup_location
    }
    url = 'https://places-dsn.algolia.net/1/places/query?countries=iso3166-2'
    response = requests.get(url, params=params).json()
    pass



lca = st.text_input('insert your location:')
st.write('Your location is:', lca)

dst = st.text_input('insert your destination:')
st.write('Your destination is:', dst)

'''
## Passengers:
'''
passenger_count = st.number_input('insert number of passengers:',min_value=0, max_value=8)

st.write('The number of passengers is: ', passenger_count)

'''
#
#
#
#
#
'''
#pickup_datetime=
#pickup_longitude=
#pickup_latitude=
#dropoff_longitude=
#dropoff_latitude=
#passenger_count=passenger_count

params = {
    'pickup_datetime' : pickup_datetime,
    'pickup_longitude' : pickup_longitude,
    'pickup_latitude' : pickup_latitude,
    'dropoff_longitude' : dropoff_longitude,
    'dropoff_latitude' : dropoff_latitude,
    'passenger_count' : passenger_count
}


'''
#
#
#
#
#
'''

url = 'https://taxifare.lewagon.ai/predict'
response = requests.get(url, params=params).json()
prediction = response['prediction']
if st.button('Get Fare !'):
    st.write(f'your estimated fare is {round(prediction,2)}')

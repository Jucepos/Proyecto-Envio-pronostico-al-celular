import pandas as pd
from twilio.rest import Client
from credenciales import TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,PHONE_NUMBER,API_KEY_WAPI
from datetime import datetime
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json



def get_date():

    input_date = datetime.now()
    input_date = input_date.strftime("%Y-%m-%d")

    return input_date

def request_wapi(api_key,query):

    url_clima = 'http://api.weatherapi.com/v1/forecast.json?key='+api_key+'&q='+query+'&days=1&aqi=no&alerts=no'

    try :
        response = requests.get(url_clima).json()
    except Exception as e:
        print(e)

    return response

def get_forecast(response,i):

    hora = int(response['forecast']['forecastday'][0]['hour'][i]['time'].split()[1].split(':')[0])
    condicion = response['forecast']['forecastday'][0]['hour'][i]['condition']['text']
    tempe = response['forecast']['forecastday'][0]['hour'][i]['temp_c']

    return hora,condicion,tempe

def create_df(data):

    col = ['Hora','Condicion','Temperatura']
    df = pd.DataFrame(data,columns=col)
    df = df.sort_values(by = 'Hora',ascending = True)
    df.set_index('Hora', inplace = True)

    return df

def send_message(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,input_date,df,query):

    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN

    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body='\nHola! \n\n\n El pronostico de lluvia hoy '+ input_date +' en ' + query +' es : \n\n\n ' + str(df),
                        from_=PHONE_NUMBER,
                        to='+34663350805'
                    )

    return message.sid

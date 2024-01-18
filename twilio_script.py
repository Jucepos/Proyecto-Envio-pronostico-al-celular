import os
from twilio.rest import Client
from credenciales import *
import time
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import requests
from tqdm import tqdm
from datetime import datetime
from twilio_funciones import request_wapi,get_forecast,create_df,send_message,get_date

query = 'Barcelona'
api_key = API_KEY_WAPI

input_date = get_date()
response = request_wapi(api_key,query) 

datos = []

for i in tqdm(range(24),colour = 'green'):

    datos.append(get_forecast(response,i))


df_final = create_df(datos)

# Send Message
message_id = send_message(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,input_date,df_final,query)


print('Mensaje Enviado con exito ' + message_id)
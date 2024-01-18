from dotenv import load_dotenv
import os

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
PHONE_NUMBER = os.getenv('PHONE_NUMBER')
API_KEY_WAPI = os.getenv('API_KEY_WAPI')

'''twilio_account_sid = os.environ.get('TWILIO_ACCOUNT_SID', TWILIO_ACCOUNT_SID)
twilio_auth_token = os.environ.get('TWILIO_AUTH_TOKEN', TWILIO_AUTH_TOKEN)
phone_number = os.environ.get('PHONE_NUMBER', PHONE_NUMBER)
api_key_wapi = os.environ.get('API_KEY_WAPI', API_KEY_WAPI)'''
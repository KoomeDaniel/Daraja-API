import requests
import json
import base64
from datetime import datetime, timedelta
import sample.config as config
import jwt

def access_token():
    response = requests.request("GET", 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials', headers={'Authorization': 'Basic cFJZcjZ6anEwaThMMXp6d1FETUxwWkIzeVBDa2hNc2M6UmYyMkJmWm9nMHFRR2xWOQ=='})
    json_data = json.loads(response.text)
    access_key = json_data.get('access_token')
    return access_key


def lipa_na_mpesa():
    access_key = access_token()

    unformatted_time = datetime.now()
    formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")

    data_to_encode = config.BusinessShortCode + config.Passkey + formatted_time
    encoded = base64.b64encode(data_to_encode.encode()).decode('utf-8')

    # Modify the Callback URL here
    callback_url = f"https://8e43-41-76-168-3.ngrok-free.app/api/payments/lnm"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_key}'
    }

    payload = {
        "BusinessShortCode": config.BusinessShortCode,
        "Password": encoded,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 1,
        "PartyA": config.Sender,
        "PartyB": config.BusinessShortCode,
        "PhoneNumber": config.Receiver,
        "CallBackURL": callback_url,
        "AccountReference": "CompanyXLTD",
        "TransactionDesc": "Payment of X"
    }

    response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers=headers, json=payload)
    print(response.text.encode('utf8'))

lipa_na_mpesa() 

def registerURL():
    access_key = access_token()
    headers = {
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {access_key}'
    }
    # Generate the JWT token
    jwt_token = generate_jwt_token()

    # Modify the Callback URL here
    callback_url = f"https://api.myapp.io/v1/results/12345?token={jwt_token}"
    payload = {
        "ShortCode": config.ShortCode,
        "ResponseType": "Completed",
        "ConfirmationURL": f"https://api.myapp.io/v1/results/12345?token={jwt_token}",
        "ValidationURL": callback_url,
    }

    response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl', headers = headers, json = payload)
    print(response.text.encode('utf8'))

# registerURL()
def c2b():
    access_key = access_token()
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {access_key}'
    }

    payload = {
        "ShortCode": 600997,
        "CommandID": "CustomerPayBillOnline",
        "Amount": 100,
        "Msisdn": 254705912645,
        "BillRefNumber": "12345678",
    }

    response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate', headers = headers, json = payload)
    print(response.text.encode('utf8'))

# c2b()
import requests
import json
import base64
from datetime import datetime, timedelta
import keys
import jwt

def access_token():
    response = requests.request("GET", 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials', headers={'Authorization': 'Basic cFJZcjZ6anEwaThMMXp6d1FETUxwWkIzeVBDa2hNc2M6UmYyMkJmWm9nMHFRR2xWOQ=='})
    json_data = json.loads(response.text)
    access_key = json_data.get('access_token')
    return access_key

def generate_jwt_token():
    # Create a payload with relevant claims (customize as needed)
    payload = {
        "sub": "user123",  # Example: User ID or relevant identifier
        "exp": datetime.now() + timedelta(minutes=30)  # Example: Token expiration time
    }

    # Sign the token using your secret key
    secret_key = "your_secret_key_here"  # Replace with your actual secret key
    jwt_token = jwt.encode(payload, secret_key, algorithm="HS256")

    return jwt_token

def lipa_na_mpesa():
    access_key = access_token()

    unformatted_time = datetime.now()
    formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")

    data_to_encode = keys.BusinessShortCode + keys.Passkey + formatted_time
    encoded = base64.b64encode(data_to_encode.encode()).decode('utf-8')
    # Generate the JWT token
    jwt_token = generate_jwt_token()

    # Modify the Callback URL here
    callback_url = f"https://api.myapp.io/v1/results/12345?token={jwt_token}"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_key}'
    }

    payload = {
        "BusinessShortCode": keys.BusinessShortCode,
        "Password": encoded,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 1,
        "PartyA": keys.Sender,
        "PartyB": keys.BusinessShortCode,
        "PhoneNumber": keys.Receiver,
        "CallBackURL": callback_url,
        "AccountReference": "CompanyXLTD",
        "TransactionDesc": "Payment of X"
    }

    response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers=headers, json=payload)
    print(response.text.encode('utf8'))

lipa_na_mpesa()

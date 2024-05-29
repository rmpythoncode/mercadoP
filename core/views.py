from django.shortcuts import render
from django.conf import settings
import requests
from django.http import JsonResponse

MERCADOPAGO_TEST_ACCESS_TOKEN = settings.MERCADOPAGO_TEST_ACCESS_TOKEN
MERCADOPAGO_TEST_PUBLIC_KEY = settings.MERCADOPAGO_TEST_PUBLIC_KEY,


def home(request):
  return render(request, 'home.html',)


def create_customer(request):
  # Customer data
  customer_data = {
      "email": "customer@example.com",
      "first_name": "John",
      "last_name": "Doe",
      "phone": {
          "area_code": "11",
          "number": "987654321"
      },
      # "address": {
      #     "zip_code": "1234567",
      #     "street_name": "Street Name",
      #     "street_number": 123
      # }
  }

  # MercadoPago API endpoint for creating customers
  create_customer_url = 'https://api.mercadopago.com/v1/customers'

  # Make POST request to create customer
  response = requests.post(create_customer_url, json=customer_data, headers={
                           "Authorization": "Bearer " + MERCADOPAGO_TEST_ACCESS_TOKEN})

  if response.status_code == 201:
    # Customer created successfully
    return JsonResponse({"status": "success", "data": response.json()}, status=201)
  else:
    print(response.json())
    # Error creating customer
    error_message = response.json().get("message", "Unknown error occurred")
    return JsonResponse({"status": "error", "error": error_message, 'message': response.json()['cause'][0]['description']}, status=response.status_code)
  return render(request, 'create_customer.html')


def delete_customer(request):
  # Customer data
  customer_data = {
      "email": "customer@example.com",
      "first_name": "John",
      "last_name": "Doe",
      "phone": {
          "area_code": "11",
          "number": "987654321"
      },
      # "address": {
      #     "zip_code": "1234567",
      #     "street_name": "Street Name",
      #     "street_number": 123
      # }
  }

  # MercadoPago API endpoint for creating customers
  delete_customer_url = 'https://api.mercadopago.com/v1/customers'

  # Make POST request to create customer
  response = requests.delete(delete_customer_url, json=customer_data, headers={
      "Authorization": "Bearer " + MERCADOPAGO_TEST_ACCESS_TOKEN})

  if response.status_code == 201:
    # Customer created successfully
    return JsonResponse({"status": "success", "data": response.json()}, status=201)
  else:
    print(response.json())
    # Error creating customer
    error_message = response.json().get("message", "Unknown error occurred")
    return JsonResponse({"status": "error", "error": error_message, 'message': response.json()['cause'][0]['description']}, status=response.status_code)
  return render(request, 'delete_customer.html')


def create_customer_js(request):

  return render(request, 'create_customer_js.html',  {
      'MERCADOPAGO_TEST_ACCESS_TOKEN': MERCADOPAGO_TEST_ACCESS_TOKEN,
      'MERCADOPAGO_TEST_PUBLIC_KEY': MERCADOPAGO_TEST_PUBLIC_KEY,
  })


def add_card(request):
  # Set your access token
  access_token = MERCADOPAGO_TEST_ACCESS_TOKEN
  # Set the customer ID
  customer_id = "YOUR_CUSTOMER_ID"

  # Define the endpoint
  url = f"https://api.mercadopago.com/v1/customers/{customer_id}/cards"

  # Card details
  card_data = {
      "token": "CARD_TOKEN",
      "issuer_id": "ISSUER_ID",  # optional
      "payment_method_id": "PAYMENT_METHOD_ID"
  }

  # Set headers
  headers = {
      "Authorization": f"Bearer {access_token}",
      "Content-Type": "application/json"
  }

  # Make the request
  response = requests.post(url, json=card_data, headers=headers)

  # Check the response status
  if response.status_code == 201:
    card = response.json()
    print("Card created successfully")
    print(
        f"Card ID: {card['id']}, Last Four Digits: {card['last_four_digits']}")
  else:
    print(f"Error: {response.status_code} - {response.json()}")
  return render(request, 'add_card.html', {
      'MERCADOPAGO_TEST_PUBLIC_KEY': MERCADOPAGO_TEST_PUBLIC_KEY,
  })


def card_token(request):
  # Set up your API credentials
  access_token = settings.MERCADOPAGO_TEST_ACCESS_TOKEN
  url = 'https://api.mercadopago.com/v1/card_tokens'

  # Collect card information
  card_data = {
      'card_number': '5031433215406351',  # Replace with the actual card number
      'expiration_month': '11',  # Replace with the expiration month
      'expiration_year': '2025',  # Replace with the expiration year
      'cardholder': {
          'name': 'Anthony Hopkins',  # Replace with the cardholder's name
          'identification': {
              # Replace with the type of identification (e.g., DNI, CPF)
              'type': 'CPF',
              'number': '25409138813'  # Replace with the identification number
          }
      }
  }

  # Make a request to MercadoPago's API
  headers = {
      'Authorization': 'Bearer ' + access_token,
      'Content-Type': 'application/json'
  }
  response = requests.post(url, json=card_data, headers=headers)
  print(response)

  # Handle the response
  if response.status_code == 201:
    card_token = response.json()['id']
    print("Card token:", card_token)
  else:
    print("Error:", response.text)
    return render(request, 'card_token.html')

  return render(request, 'card_token.html')

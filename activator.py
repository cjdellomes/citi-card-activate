import requests
import config

request_url = 'https://www.cardactivation.citi.com/Home/Continue1'
request_headers = {
    'Accept': 'application/json, text/javascript',
    'Host': 'www.cardactivation.citi.com',
    'Content-Type': 'application/json; charset=UTF-8',
    'Origin': 'https://www.cardactivation.citi.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}
request_data = {
    'cardNumber': config.card_number,
    'securityCode': config.security_code
}

r = requests.post(request_url, data=request_data, headers=request_headers)

print(r.status_code)
print(r.text)
print(r.json())

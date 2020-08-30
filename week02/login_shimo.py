import requests
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
headers = {
    'user-agent': ua.random,
    'origin': 'https://shimo.im',
    'referer': 'https://shimo.im/login?from=home',
    'x-requested-with': 'XmlHttpRequest',
    'x-source': 'lizard-desktop'
}

s = requests.Session()

login_url = 'https://shimo.im/lizard-api/auth/password/login'
form_data = {
    'mobile': '+86134*******7',
    'password': 't*****3'
}

response = s.post(login_url, data=form_data, headers=headers)
print(response.status_code)
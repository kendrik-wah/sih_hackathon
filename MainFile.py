from bs4 import BeautifulSoup
import json, random, re, requests

BASE_URL = 'https://www.instagram.com/accounts/login/'
LOGIN_URL = BASE_URL + 'ajax/'

headers_list = [
        "Mozilla/5.0 (Windows NT 5.1; rv:41.0) Gecko/20100101"\
        " Firefox/41.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2)"\
        " AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2"\
        " Safari/601.3.9",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0)"\
        " Gecko/20100101 Firefox/15.0.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"\
        " (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36"\
        " Edge/12.246"
        ]

USERNAME = 'kendrik_wah@yahoo.com.sg'
PASSWD = 'magnataur'
USER_AGENT = headers_list[random.randrange(0,4)]

session = requests.Session()
session.headers = {'user-agent': USER_AGENT}
session.headers.update({'Referer': BASE_URL})
req = session.get(BASE_URL)
soup = BeautifulSoup(req.content, 'html.parser')
body = soup.find('body')

pattern = re.compile('window._sharedData')
script = body.find("script", text=pattern)

script = script.get_text().replace('window._sharedData = ', '')[:-1]
data = json.loads(script)

csrf = data['config'].get('csrf_token')
login_data = {'username': USERNAME, 'password': PASSWD}
session.headers.update({'X-CSRFToken': csrf})
login = session.post(LOGIN_URL, data=login_data, allow_redirects=True)
print(login.content)
print(login)

print(" ")
print(" ")
new_session = requests.Session()
accessing_eatbook_instagram = new_session.get("https://www.instagram.com/kendrikwah/")
new_soup = BeautifulSoup(accessing_eatbook_instagram.content, 'html.parser')
new_body = soup.find('body')

print(new_body)
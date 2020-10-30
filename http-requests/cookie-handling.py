from urllib.request import build_opener, HTTPCookieProcessor
from http.cookiejar import CookieJar, FileCookieJar
from pprint import pprint
from datetime import datetime

cookie_jar = CookieJar()
# file_cookie_jar = FileCookieJar('cookies.txt')

url_opener = build_opener(HTTPCookieProcessor(cookie_jar))

response = url_opener.open('https://github.com')

print(len(cookie_jar), 'Cookies are set')
# print(len(file_cookie_jar), 'Cookies are set')

for cookie in cookie_jar:
    print(f'name={cookie.name} value={cookie.value} domain={cookie.domain} path={cookie.path} exp={cookie.expires} secure={cookie.secure}')
    try:
        dt = datetime.fromtimestamp(cookie.expires)
        print('Expires', dt)
        print()
    except TypeError as e:
        # print(e)
        pass

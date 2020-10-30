from urllib.request import urlopen

resp = urlopen('https://www.python.org')

print(resp.headers)

mime_type, encoding = resp.getheader('Content-Type').split(';')
encoding = encoding.split('=')[1].strip()

print(mime_type, encoding)

payload = resp.read().decode(encoding)

print(payload[:42])

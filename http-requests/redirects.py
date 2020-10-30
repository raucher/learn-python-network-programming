from urllib.request import urlopen, Request


req = Request('https://gmail.com')


resp = urlopen(req)

print('Initial request:', req.get_full_url())
print('Response after redirects:', resp.url)

# redirect response (301, 302, 303, 307, ...)
# has header
# Location: redirect.url

# Request object erfasst Redirektionen
print(req.redirect_dict)

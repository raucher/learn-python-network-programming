from urllib.request import urlopen
from urllib.error import HTTPError, URLError

# urlopen() throws an HTTPError exception on HTTP errors
# URLError on
try:
    resp = urlopen("https://www.ietf.org/rfc/rfc0.txt")  # 404 error
except HTTPError as e:
    print("URL:", e.url)
    print("code:", e.code)
    print("reason:", e.reason)


# If something goes wrong lower in the network stack,
# then the appropriate module will raise an exception.
# The urllib package catches these exceptions and then
# wraps them as URLErrors.
try:
    resp = urlopen("https://not.existing.url")
except URLError as e:
    print(e)  # <urlopen error [Errno 11001] getaddrinfo failed>

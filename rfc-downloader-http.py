import sys
from urllib import request

try:
    rfc_number = int(sys.argv[1])
except (IndexError, ValueError):
    print("Must supply RFC number as first argument")
    exit(2)

url = f'https://www.ietf.org/rfc/rfc{rfc_number}.txt'
rfc_raw = request.urlopen(url).read() # BYTE string
# print(rfc_raw)

rfc_content = rfc_raw.decode() # Now as Unicode
print(rfc_content)

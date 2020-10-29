from urllib.request import Request
from urllib.request import urlopen
import gzip

headers = {
    'Accept-Language': 'sv',
    # 'Accept-Encoding': 'gzip',  # Tell server that client supports gzip
    # 'Accept-Encoding': 'identity',  # Tell server that client doesn't want any encoding,

    # relative weightings can be given to specific encodings by adding a q value
    # The maximum q value is 1.0, and this is also the default if no q value is given.
    'Accept-Encoding': 'gzip, deflate;q=0.0, idenity;q=0.0'
}
req = Request("https://www.debian.org", headers=headers)
# req.add_header("Accept-Language", "sv")

print("Request Headers:", req.header_items())


resp = urlopen(req)

print(resp)
print("\n----- Response Headers -----", resp.headers, sep="\n")
print("Content Encoding ->", resp.getheader('Content-Encoding'))

data = resp.read()

print("\nEncoded:\n", data.splitlines()[:3])  # gzip encoded data

# Decode GZIP
try:
    print("\nDecoded:\n", gzip.decompress(data).splitlines()[:3])
except:
    print("Content is not decoded")

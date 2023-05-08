import hashlib

# def check_key(key, username_trial):
#     global key_full_template_trial
#     if len(key) != len(key_full_template_trial):
#         return False
#     else:
#         # Check static base key part --v
#         i = 0
#         for c in key_part_static1_trial:
#             if key[i] != c:
#                 return False
#             i += 1
#         # TODO : test performance on toolbox container
#         # Check dynamic part --v
#         if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
#             return False
#         else:
#             i += 1
#         if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
#             return False
#         else:
#             i += 1
#         if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
#             return False
#         else:
#             i += 1
#         if key[i] != hashlib.sha256(username_trial).hexdigest()[6]:
#             return False
#         else:
#             i += 1
#         if key[i] != hashlib.sha256(username_trial).hexdigest()[2]:
#             return False
#         else:
#             i += 1
#         if key[i] != hashlib.sha256(username_trial).hexdigest()[7]:
#             return False
#         else:
#             i += 1
#         if key[i] != hashlib.sha256(username_trial).hexdigest()[1]:
#             return False
#         else:
#             i += 1
#         if key[i] != hashlib.sha256(username_trial).hexdigest()[8]:
#             return False

#         return True


username_trial = b"vishwaCTF"

key = "VishwaCTF{m4k3_it_possibl3_"
key += hashlib.sha256(username_trial).hexdigest()[4]
key += hashlib.sha256(username_trial).hexdigest()[5]
key += hashlib.sha256(username_trial).hexdigest()[3]
key += hashlib.sha256(username_trial).hexdigest()[6]
key += hashlib.sha256(username_trial).hexdigest()[2]
key += hashlib.sha256(username_trial).hexdigest()[7]
key += hashlib.sha256(username_trial).hexdigest()[1]
key += hashlib.sha256(username_trial).hexdigest()[8]
key += "}"
print(key)
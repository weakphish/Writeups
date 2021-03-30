import hashlib

name = "MORTON".encode()
key = "picoCTF{1n_7h3_|<3y_of_"

key += hashlib.sha256(name).hexdigest()[4]
key += hashlib.sha256(name).hexdigest()[5]
key += hashlib.sha256(name).hexdigest()[3]
key += hashlib.sha256(name).hexdigest()[6]
key += hashlib.sha256(name).hexdigest()[2]
key += hashlib.sha256(name).hexdigest()[7]
key += hashlib.sha256(name).hexdigest()[1]
key += hashlib.sha256(name).hexdigest()[8]

key += "}"

print(key)

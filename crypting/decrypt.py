import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "encrypt.py" or file == "secretkey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("secretkey.key" "rb") as key:
    secretkey = key.read()

for file in files:
    with open(file, "rb") as thefile:
        contests = thefile.read()
    contests_decrypted = Fernet(secretkey).decrypt(contests)
    with open(file, "wb") as thefile:
        thefile.write(contests_decrypted)



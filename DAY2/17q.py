print("\nCaesar Cipher Encryption and Decryption")
text=input("Enter text: ")
key=int(input("Enter key: "))

print("Encrypted Text:")
enc=""
for c in text:
    if c.isalpha():
        o=65 if c.isupper() else 97
        enc+=chr((ord(c)-o+key)%26+o)
    else:
        enc+=c
print(enc)

print("Decrypted Text:")
dec=""
for c in enc:
    if c.isalpha():
        o=65 if c.isupper() else 97
        dec+=chr((ord(c)-o-key)%26+o)
    else:
        dec+=c
print(dec)
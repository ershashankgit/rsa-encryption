import rsa

with open("public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

print("Text Encryption With RSA Keys ")
print("1. Encrypt \n2. Decrypt")
ch = int(input("Enter your Choice: "))

if ch==1:
    message = input("Enter Message: ")
    ciphertext = rsa.encrypt(message.encode(), public_key)
    with open("encryptedmsg.dat", "wb") as f:
        f.write(ciphertext)
    print(ciphertext)

elif ch==2:
    enc_msg = open("encryptedmsg.dat", "rb").read()
    print("Encrypted Message:\n",enc_msg)
    clear_msg = rsa.decrypt(enc_msg, private_key)
    print(f'\nPlain text: {clear_msg.decode()}\n')
else:
    print("Wrong Choice!")


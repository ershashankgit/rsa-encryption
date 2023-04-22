import rsa

def generateKeys():
    (publicKey, privateKey) = rsa.newkeys(2048)
    with open('public.pem', 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open('private.pem', 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))
    
generateKeys()



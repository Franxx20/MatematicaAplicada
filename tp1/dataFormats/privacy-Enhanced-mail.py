from Crypto.PublicKey import RSA

public_key = RSA.import_key(open("privacy_enhanced_mail.pem",'r').read()).d
print(public_key)

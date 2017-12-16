import base58

# translate traditional address to Copay's address format
trad_address = '19oCM37SX7R7ctVPwv1pQ2RckTM3TmU9dS'
public_key_hash = base58.decodeBase58Check(trad_address,0)
copay_address = base58.encodeBase58Check(public_key_hash,28)
print "Copay Address: ", copay_address



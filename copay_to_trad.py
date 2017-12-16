import base58

# translate Copay's address format to traditional address format
copay_address = 'CQ6BSmiDScwR3HX3pLaDdMjcMdz8byfKRo'
public_key_hash = base58.decodeBase58Check(copay_address,28)
trad_address = base58.encodeBase58Check(public_key_hash,0)
print "Traditional Address: ", trad_address

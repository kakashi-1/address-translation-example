from crypto import Key, SHA256, RIPEMD160
import base58

def readPrivateKey(filename):
	with open(filename, "rb") as f:
		privateKey = f.read()
	privateKey = privateKey.split("\n")[0] #first line
	privateKey = privateKey.strip() #ignore whitespace
	return base58.decodeBase58Check(privateKey, 128) #PRIVKEY = 128

def getCopayAddress(key):
	publicKeyHash = RIPEMD160(SHA256(key.getPublicKey()))
	return base58.encodeBase58Check(publicKeyHash,28) 

def getTraditionalAddress(key):
	publicKeyHash = RIPEMD160(SHA256(key.getPublicKey()))
	return base58.encodeBase58Check(publicKeyHash,0) #PUBKEY_ADDRESS = 0

# get traditional address using a public key (given a private key)
privateKey = readPrivateKey('key.txt')
k = Key()
k.setPrivateKey(privateKey)
trad_address = getTraditionalAddress(k)
print "Public key: ", k.getPublicKey().encode("hex")
print "Public Key Hash  " + RIPEMD160(SHA256(k.getPublicKey())).encode("hex")
print "Traditional Address: ", trad_address

# translate traditional address to Copay's address format
public_key_hash = base58.decodeBase58Check(trad_address,0)
copay_address = base58.encodeBase58Check(public_key_hash,28)
print "Copay Address: ", copay_address

# translate Copay's address format to traditional address format
public_key_hash = base58.decodeBase58Check(copay_address,28)
trad_address = base58.encodeBase58Check(public_key_hash,0)
print "Traditional Address: ", trad_address


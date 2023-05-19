from Crypto.Cipher import AES
import binascii

raw = '37f31f045120e0b586acb60f652089924faf98a4c87698a64dd5518fa5cb51c52c1d7d7c9dc4f5ea6074d9186ea7b473814cab3320e5db7a5107780be1898d050c32aa3d48d3eceb1da3dc355d67da1df5f2e964b40bf24200686e5ec8d41d56' 

# Ensure that raw has even length
if len(raw) % 2 != 0:
    raw = '0' + raw

ciphertext = binascii.unhexlify(raw.replace(' ','')) 

# The key and IV need to be bytes.
key = b'ijklmnopqrstuvwx'

# The IV should be unique and secure, but for this example, I'm using a constant one.
iv=binascii.unhexlify('00000000000000000000000000000000')
#iv=binascii.unhexlify('d63b4ad6f6d9ac9b608ec8b42734b1ca')


obj = AES.new(key, AES.MODE_CBC, iv) 

# Decrypt and print the plaintext.
plaintext = obj.decrypt(ciphertext)
print('Plaintext is:\n' + plaintext.decode('utf-8', errors='ignore')) 

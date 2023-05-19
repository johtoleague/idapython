import base64

s = ""
custom = 'CDEFGHIJKLMNOPQRSTUVWXYZABcdefghijklmnopqrstuvwxyzab0123456789+/'
base64_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

ciphertext = 'BInaEi=='

for ch in ciphertext:
    if ch in custom:
        s += base64_chars[custom.index(ch)]
    elif ch == '=':
        s += '='

# Convert the string s to bytes
s = s.encode()

# Use base64.b64decode to decode the string
print(base64.b64decode(s).decode('utf-8'))

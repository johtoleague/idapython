def ror13(value):
    for _ in range(13):
        lsb = value & 0x1
        value >>= 1
        if lsb != 0:
            value |= (1 << 31)
    return value

def decode_hash(encoded):
    hex_encoded = int(encoded, 16) # Convert the input from hex to int
    decoded_int = ror13(hex_encoded) # Apply ROR-13
    return hex(decoded_int) # Convert back to hex and return

print(decode_hash("EC0E4E8E"))

def ror(dword, bits):
    return (dword >> bits | dword << (32 - bits)) & 0xFFFFFFFF

def get_hash(name):
    result = 0
    for c in name:
        result = ror(result, 13)
        result += ord(c)
    return hex(result)

# Calculate the hash for 'LoadLibraryA'
hash_value = get_hash('LoadLibraryA')
print(hash_value)

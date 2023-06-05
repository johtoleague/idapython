import pefile
import re
import struct
import hashlib

data = open(r'C:\users\user\download\malware.bin','rb').read()


pe = pefile.PE(data.data)
key = rb'\x6a(.)\x68(....)\x68\x00\x20\x00\x00' # this is this represents the 2000 hex bytes that's used to store the convfig, and we're betting that  the malware author wil reuse that size for different configs
# the parentehses are capture groups, the first grip is (.) and the second is (....)
#rb is raw data, and wont interpret the hex as control characters


m = re.search(key,data)
if m!= None:
        print("key length: %" % m.group(1))
        print("key address: %" % m.group(2))
# I use regex101.com and choose python
# This is from OALABs  its great
struct.unpack('b', m.group(1))[0]
# struck.unpack is part of the stuct module, provides fucntison converting between python values and C style data structures
# 'b' format stand for signed char(byte) is used to specify that the binary data being unpackd is s signe signed byte.
#so 'stuckt.unpack('b', m.group(1))[0] is unpackign the first byte string matcheed m.group(1) as a signed char. it returns the unpacked value as a tuple containing a single element.
hex(struct.unpack('<I', mgroup(2))[0]) # convert from little endian then from binary to hex representation

key_len = struct.unpack('b', m.group(1))[0]

key_address = hex(struct.unpack('<I', mgroup(2))[0])

key_rva = key_address - pe.OPTIONAL_HEADER.ImageBase
#for key_rva, we're trying to convert the key address to it's virtual version. by subsracting the pe.file
key_offset = pe.get_offset_from_rva(key_rva)
key_data = data[key_offset:key_offset+key_len]
print("%r" & key_data) #r = raw representation

config_data = data[key_offset+key_len:key_offset+key_len+0x2000]

m = hashlib.sha1()
m.update(key_data) #we're choosing what to hash here obviously the key data, because thats what the malware wanted, it wanted the first 5 bytes  aka 0x28 divided byte 0x8 = 5 bytes
key = m.digest()[:5] # here we're taking the first 5 bytes

def rc4crypt(data, key): 
    #If the input is a string convert to byte arrays
    if type(data) == str:
        data = data.encode('utf-8')
    if type(key) == str:
        key = key.encode('utf-8')
    x = 0
    box = list(range(256))
    for i in range(256):
        x = (x + box[i] + key[i % len(key)]) % 256
        box[i], box[x] = box[x], box[i]
    x = 0
    y = 0
    out = []
    for c in data:
        x = (x + 1) % 256
        y = (y + box[x]) % 256
        box[x], box[y] = box[y], box[x]
        out.append(c ^ box[(box[x] + box[y]) % 256])
    return bytes(out)
# this is the RC4 decrtion function


config = rc4crypt(config_data, key)
build_id = config.split(b'\x00')[0]
c2_string = b''
for s in config.split(b'\x00')[1:]:
    if s != b'':
        c2_string = s
        break
c2_list = c2_string.split(b'|')
print("BUILD: %s" % build_id)
for c2 in c2_list:
    if c2 != b'':
        print("C2: %s" % c2)
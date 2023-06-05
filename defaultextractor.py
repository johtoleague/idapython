import pefile
import re
import struct
import hashlib

data = open(r'C:\users\user\download\malware.bin','rb').read()


pe = pefile.PE(data.data)
key = b'\x6a(.)\x68(....)\x68\x00\x20\x00\x00' # this is this represents the 2000 hex bytes that's used to store the convfig, and we're betting that  the malware author wil reuse that size for different configs
# the parentehses are capture groups, the first grip is (.) and the second is (....)

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


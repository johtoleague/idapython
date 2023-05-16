#from PMA
import idaapi
def NopBytes(start, length):
	for i in range(0, length):
		Patch_Byte(start + i, 0x90)
	MakeCode(start)



NopBytes(0x004011C0, 4) #nop starting at this address and 4 bytes forward
NopBytes(0x004011C6, 3)
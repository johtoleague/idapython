x = open("yeet", "wb")  
x.write(read_dbg_memory(get_reg_value('rbx'), 0x10600))  
x.close()
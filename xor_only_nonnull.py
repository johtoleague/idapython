def xor_file(input_file, output_file, key):
    with open(input_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            while True:
                byte = f_in.read(1)
                if not byte:
                    break  # End of file reached
                xored_byte = ord(byte) ^ key
                if xored_byte != 0:
                    f_out.write(bytes([xored_byte]))
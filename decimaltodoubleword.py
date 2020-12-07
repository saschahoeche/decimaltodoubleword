from typing import NoReturn


def ddConverter(decimalInput):
    '''
    Takes a decimal integer and returns a list of decimal byte values\n
    100 -> 0000.0000.0000.0000.0000.0000.0110.0100 -> Byte22=0, Byte21=0, Byte20=0, Byte19=100\n
    '''
    byteDecimal = bin(decimalInput)
    
    # pad with zeros to fill 4 bytes
    fourByteDecimal = str(byteDecimal[2:]).zfill(32)
    
    # seperate in four bytes
    byte22 = int(fourByteDecimal[:8], 2)
    byte21 = int(fourByteDecimal[9:16], 2)
    byte20 = int(fourByteDecimal[17:24], 2)
    byte19 = int(fourByteDecimal[24:], 2)
    
    print(byte22, byte21, byte20, byte19)
    
    ### TODO return decimal byte list, implement negativ input (pos val -255)
    
    return fourByteDecimal

print(ddConverter(-30000))
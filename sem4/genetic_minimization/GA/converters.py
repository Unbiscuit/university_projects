from codecs import decode
import struct
import numpy as np
import math

# convert binary number to float
def bin_to_float(b):
    bf = struct.unpack('!f',struct.pack('!I', int(b, 2)))[0]
    return bf

# convert float number to binary
def float_to_bin(value):
    d = bin(struct.unpack('!I', struct.pack('!f', value))[0])[2:].zfill(32)
    return d
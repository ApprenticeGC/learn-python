#! /usr/local/bin/python3.2
var01 = 10
var02 = 20

var03 = bin(var01)
var04 = oct(var02)
var05 = var01 / var02
var06 = var01 // var02
print(var01)
print(var02)
print(var03)
print(var04)
print(var05)
print(var06)

# 1224 has to be in (), it is an error if not inside ()
var07 = (1224).bit_length()
print(var07)

var08 = True
var09 = False
print(var08 and var09)

# The following expression will generate error
#print(sys.float_info)

var10 = 20 + 55.4j
print(var10)
print(var10.real, var10.imag)

import decimal
var11 = decimal.Decimal(32354)
print(var11)

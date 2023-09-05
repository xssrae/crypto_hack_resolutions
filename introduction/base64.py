#!/usr/bin/env python3
import sys
import base64


if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

encript = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

bytes.fromhex(encript) # hex-string => bytes
decript = base64.b64encode(encript) # bytes => base64

print("Here is your flag:")
print(decript)

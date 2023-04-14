import base64
hexFlag = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
bytesFlag = bytes.fromhex(hexFlag)

base64Flag = base64.b64encode(bytesFlag)
print(base64Flag)

# base64.encode(bytesFlag,base64Flag)

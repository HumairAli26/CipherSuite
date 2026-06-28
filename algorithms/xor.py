def xor(inpString, key):
    length = len(inpString)

    for i in range(length):
        inpString = (inpString[:i] + chr(ord(inpString[i]) ^ ord(key)) +inpString[i + 1:])
        print(inpString[i], end = "")
    
    return inpString
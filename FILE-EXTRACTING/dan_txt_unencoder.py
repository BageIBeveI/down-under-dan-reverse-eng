import glob
import os

unencBytes = b''
danUnencodedTxt = "danUnencodedTxt"
danOutput = "danoutput"

if not os.path.exists(danUnencodedTxt):
    os.makedirs(danUnencodedTxt)

#name = input("input .ENC filename (without the .enc): ")
startLen = len(f"{danOutput}/SO\\")
for txtfile in glob.glob(f"{danOutput}/SO/*.ENC"):
    txtname = txtfile[startLen:-4]
    unencBytes = b''
    with open(txtfile, "rb") as encfile:
        encBytes = encfile.read()
        for byte in encBytes:
            unencBytes += (byte ^ 186).to_bytes(1)

    with open(f"{danUnencodedTxt}/{txtname}.txt", "wb") as txtfile:
        txtfile.write(unencBytes)

    print(unencBytes)


"""
input = "82 8C 96 83 8C 96 8D 8C 96 8B 8A 8B 96 8F 8C 96 8B 8A 8B 96 8E 8F 96 82 89 96 8F 96 83 8E 96 88 8A 96 83 82 96 8C 82 96 83 82 96 8B 8A 8A 96 8B 88 8A 96 88 8A 8A 96 88 8A 8A 96 8B 8E 8F 96 88 8E 88 96 82 8A 96 88 89 88 96 8D 8A 96 88 89 88 96 83 83 83 83 88 8A 96 8B 8D 8A 96 8B 8F 8E 96 8B 82 8E 96 88 8A 96 88 8B 8E 96 88 83 8C 96 88 88 88 96 83 83 83 83 8B 8D 8E 96 8B 8C 89 96 8B 8D 8E 96 8B 88 8C 96 8B 8E 96 8B 8C 8A 96 8B 8B 8F 96 8B 8C 88 96 83 83 83 83 89 82 96 8B 8B 82 96 89 82 96 8B 88 8A 96 8D 8C 96 8B 88 8A 96 8D 8C 96 8B 8E 82 96 8D 8C 96 8B 8F 8A 96 83 83 83 83 8D 8C 96 8B 8F 8A 96 8D 8C 96 8B 88 8A 96 89 82 96 8B 88 8A 96 89 8D 96 8B 88 8A 96 83 83 83 83 88 8E 82 96 83 82 96 88 8B 82 96 8B 8A 83 96 82 8A 96 8B 89 8A 96 82 8A 96 8B 89 8C 96 82 8A 96 8B 89 82 96 83 83 83 83 88 8B 82 96 8B 8A 83 96 88 8E 82 96 83 82 96 88 8A 82 96 82 82 96 88 8A 8C 96 82 82 96 83 83 83 83 88 83 96 88 8B 8F 96 82 82 96 88 8A 8D 96 8B 82 8F 96 88 8B 8B 96 88 8D 8F 96 8B 8C 83 96 88 8D 8F 96 8B 8D 8A 96 83 83 83 83 88 89 96 8B 8E 8B 96 8B 8A 8C 96 8B 8E 8F 96 88 8A 88 96 8B 83 88 96 88 82 8C 96 8B 82 83 96 88 82 8C 96 8B 83 8A 96 83 83 83 83 88 8E 8A 96 8B 8E 88 96 88 8D 82 96 8B 8D 88 96 82 8A 96 8B 82 8E 96 8E 8C 96 88 8A 88 96 8E 8C 96 88 8A 8E 96 83 83 83 83 8A 96 8F 8A 96 8F 8A 96 8B 8A 8A 96 88 8A 8A 96 8F 8A 96 8A 96 8F 8A 96 88 88 8A 96 83 8A 96 8B 8A 8A 96 8F 8A 96 8A 96 8F 8A 96 83 83 83 83 8B 8E 8E 96 8B 8F 8C 96 89 8A 8C 96 8B 8F 8C 96 88 8E 82 96 8B 8D 8D 96 89 8A 8C 96 8B 83 8E 96 8B 8B 88 96 88 89 8A 96 89 8A 8C 96 8B 8F 8C 96 8B 8E 8E 96 8B 8F 8C 96 83 83 83 83 8D 8C 96 8B 8F 8A 96 8D 8C 96 8B 88 8A 96 8B 8A 82 96 8B 88 8A 96 8B 8A 8D 96 8B 88 8A 96 83 83 83 83 8E 82 96 8B 8C 88 96 89 8B 8A 96 8B 8D 82 96 8B 8C 96 88 88 8A 96 88 8D 8A 96 88 88 8E 96 89 8E 96 8B 82 88 96 89 8B 8A 96 8B 8D 82 96 8E 82 96 8B 8C 88 96 83 83 83 83 8E 8A 96 88 88 8F 96 8E 8A 96 88 89 8A 96 8C 8A 96 88 89 8A 96 8E 8A 96 88 88 8F 96 8C 8A 96 88 88 8A 96 8E 8A 96 88 88 8A 96 8E 8A 96 88 88 8F 96 83 83 83 83"
bytelist = b''
for byte in input.split(" "):
    bytelist += int(byte, 16).to_bytes(1)


stringy = ""
nowThisIsAList = [b''] * 0x100
for value in range(0, 0x100):
    for encoded in bytelist:
        nowThisIsAList[value] += (encoded ^ value).to_bytes(1)
    print(nowThisIsAList[value], value, "\n")
"""
#xor by 186, though 154 is kinda close? maybe ascii has some cool symmetry that idk about, or maybe xor does?


#for real this time then
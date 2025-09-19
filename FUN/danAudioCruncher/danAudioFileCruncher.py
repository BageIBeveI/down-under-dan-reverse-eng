### This script patches Down Under Dan's audio files, changing them into
### (I think) the faulty ones MikePanoots used.

### You'll need to place your audio files into the input folder,
### and you'll get the patched ones from the output folder.

### Remember to unzip the difference folder!
import os

if not os.path.isdir("input"):
    os.mkdir("input")
if not os.path.isdir("output"):
    os.mkdir("output")
if not os.path.isdir("difference"):
    os.mkdir("difference")
    
    
fileNames = ["1TO3.1", "3TO6.1", "6TO9.1", "9TO12.1", "12TO15.1", "15TO18.1", "18TO21.1"]


def crunchify(filename):
    # i dunno why fully rewriting is faster than copying and editing, but i'll take it

    with open(f"input/{filename}", 'rb') as inputAudioFile:
        audioData = inputAudioFile.read()

        with open(f"difference/{filename.lower()[0:-1]}difference", 'rb') as differenceFile:
            differences = differenceFile.read()

            with open(f"output/{filename.lower()}", 'wb') as outputAudioFile:

                headerSize = 3
                adrDiffSize = 2
                byteSize = 1

                nextChangedAddress = 0

                # first 3 bytes of differences are the whole file length
                fileLength = int.from_bytes(differences[0:headerSize], 'little')

                #then in chunks of 2,1 bytes, starting at offset 3, get addressDifference and new value
                diffOffset = headerSize

                nextChangedAddress += int.from_bytes(differences[diffOffset:diffOffset + adrDiffSize], 'little')
                nextChangedValue = differences[diffOffset + adrDiffSize]

                diffOffset += (adrDiffSize + byteSize)

                for byteIndex in range(fileLength):

                    # if we found the right address, write the modified value
                    if byteIndex == nextChangedAddress:
                        outputAudioFile.write(nextChangedValue.to_bytes(byteSize, 'little'))

                        try:
                            nextChangedAddress += int.from_bytes(differences[diffOffset:diffOffset + adrDiffSize], 'little')
                            nextChangedValue = differences[diffOffset + adrDiffSize]
                        except IndexError:
                            pass

                        diffOffset += (adrDiffSize + byteSize)

                    # otherwise, write the regular value
                    else:
                        outputAudioFile.write(audioData[byteIndex].to_bytes(1, 'little'))

        print(f"{filename} modified successfully.")


for file in fileNames:
    if os.path.exists(f"input/{file}") and os.path.exists(f"difference/{file[0:-1]}difference"):
        crunchify(file)
    else:
        print(f"{file} or difference file not found.")


input("\n\nDone! Any found files are now in the output folder, and can be copied back into where your input came from.\
        \n(Press enter twice to close console.)")





### just leaving the code to make the differences here
### prob won't be useful to anyone, but good to have in case it needs to change
"""
fileNames = ["1TO3.1", "3TO6.1", "6TO9.1", "9TO12.1", "12TO15.1", "15TO18.1", "18TO21.1"]

if not os.path.isdir("original"):
    os.mkdir("original")
if not os.path.isdir("crunched"):
    os.mkdir("crunched")
if not os.path.isdir("difference"):
    os.mkdir("difference")

for filename in fileNames:

    with open(f"original/{filename}", 'rb') as audioFile1:
        audioData1 = audioFile1.read()

        with open(f"crunched/{filename.lower()}", 'rb') as audioFile2:

            audioData2 = audioFile2.read()

            numBytes = len(audioData2)

            changingBytes = [numBytes.to_bytes(3, 'little')]

            previousAddress = 0

            # check each byte. if not equal log it
            for x in range(numBytes):
                if audioData2[x]!=audioData1[x]:
                    # instead of storing addresses, store differences
                    # that lets it be 2 bytes max, so it doesn't exceed the github filesize limit
                    addressDifference = (x - previousAddress).to_bytes(2, 'little')
                    previousAddress = x

                    value = audioData2[x].to_bytes(1, 'little')

                    changingBytes.append(addressDifference+value)


        with open(f"difference/{filename[0:-1]}difference", 'wb') as writeFile:
            for twelveFour in changingBytes:
                writeFile.write(twelveFour)


#"""
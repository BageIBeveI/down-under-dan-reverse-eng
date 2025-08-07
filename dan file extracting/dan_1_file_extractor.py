import os #needed to make a file in the new directory

if not os.path.exists(f"daninput"):
    os.makedirs("daninput")
if not os.path.exists(f"danoutput"):
    os.makedirs("danoutput")

for danfile in ['1TO3.1', '3TO6.1', '6TO9.1', '9TO12.1', '12TO15.1', '15TO18.1', '18TO21.1', 'BACK.1', 'IM.1', 'MISC.1', 'MUST.1', 'OBJVOC.1', 'PLTA.1', 'RIVA.1', 'RIVB.1', 'SHER.1', 'SO.1']: #big loop for every dan .1 file
    try:
        f = open(f"daninput/{danfile}", 'rb')
        hexfile = f.read()
        f.close()                        #turns the dan file into bytes and stores it in hexfile

        if not os.path.exists(f"danoutput/"+ str(danfile[0:-2])):
            os.makedirs("danoutput/"+ str(danfile[0:-2]))     #makes the folder for the files in its own directory instead of cluttering current folder.

        file_names = []                  #will store the names of individual dan subfiles
        file_offsets = []                #will store the offset of where the dan subfile bytes start
        file_sizes = []                  #will store how many bytes long each subfile is

        start_at = int.from_bytes(hexfile[142:146], 'little', signed=False)       #start_at = first subfile offset: the GX library starts that part of the file allocation table here
                                                                                  #and also the bytes are stored in the little endian format, sign doesn't matter i dont think

        for i in range(128, start_at, 26):             #the names start at offset 128 and end a bit before the actual subfile data starts, and each FAT
                                                       #line is 26 bytes long in the GX library
                                                       #(1 is a space, 12 are for the name, another 1 space, 4 for the offset, 4 for the size, 2 for the date, 2 for the time)
            datastoringstring = ''                     #this string will store the file name, and this both creates it and resets it so it can store a new name
            for j in range(i + 1, i + 13):                #the name is stored between i + 1 and i + 13, so this loop adds the rest of the characters to datastoringstring
                if hexfile[j] != 32:                      #as long as the hex value isn't 0d32 aka 0x20, which is a blank space (which clutters up some of the audio names),
                    datastoringstring = datastoringstring + (chr(hexfile[j]))         #add the character to the string (def not the best way, but it works)
            file_names.append(datastoringstring)
            file_offsets.append(int.from_bytes(hexfile[i + 14:i + 18], 'little', signed=False))    #the name is stored between i+14 and i + 17, so this adds it to the offset list
            file_sizes.append(int.from_bytes(hexfile[i + 18:i + 22], 'little', signed=False))      #the file size is stored between i+18 and i+21



        for k in range(0, len(file_names)):                 #for however many subfiles are in the .1 file,
            badFlag = False  #flag so the 002 003 004 files don't have the same names (for mp3 conversion)
            if file_names[k][-1:] in "2345":
                badFlag = True
            if badFlag:
                file_dir_and_name = "danoutput/" + str(danfile[0:-2] + "/" + file_names[k][0:-4] + "-" + file_names[k][-1] + file_names[k][-4:-1] + file_names[k][-1])
            else:
                file_dir_and_name = "danoutput/" + str(danfile[0:-2] + "/" + file_names[k])     #store the directory with file name for each subfile in this variable
            f = open(file_dir_and_name, 'wb')                                         #make a file for that subfile using the afforementioned path
            f.write(hexfile[file_offsets[k]:file_offsets[k] + file_sizes[k]])     #add the hex bytes from the first byte's offset : the last byte's offset (== offset + size) (in old python it needed a +1 i think? idk it worked then but now it adds an extra byte, so the +1 is gone)
        f.close()      #close the file directory, and repeat it all again
    except FileNotFoundError:
        print(danfile + " not found in daninput folder.")
    except Exception:
        print("Error!")
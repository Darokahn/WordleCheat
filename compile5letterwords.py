with open("new_dict.txt", "w") as newfile:
    with open("en_US.dic", "r") as file:
        for newline in file.readlines():
            stop = newline.find("/")
            newline = newline[:stop]
            newline = newline.replace("'", "")
            if len(newline) == 5:
                newfile.write(newline + "\n")
            newline = file.readline()
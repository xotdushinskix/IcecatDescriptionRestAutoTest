class ReadAccessKeyFile():

    def fileReader(self):
        nameFile = open("accesskey.txt")
        textFromFile = nameFile.read()
        return textFromFile

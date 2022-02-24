class textEditor:
    def __init__(self, filePath, usingJson = False):
        self.filePath = filePath
        self.fileType = None
        self.fileContents = None
        self.getFileType(usingJson)
        self.getFileContents()
    
    def getFileType(self, usingJson = False): #Works
        '''Determines file type'''
        split = self.filePath.split('.')
        end = split[-1]
        self.fileType = end
        if self.fileType == 'json' and usingJson == False:
            raise Exception("Using textEditor on json files is not recommended due to curly braces and square braces.\nIf you still wish to proceed make usingJason = True.")
            
    
    def getFileContents(self):
        '''Gets content of files, to not erase them'''
        try:
            self.fileContents = open(self.filePath, "r").read()
        except:
            self.fileContents = open(self.filePath, "w")
            self.fileContents = open(self.filePath, "r").read()
    
#<----------------------------------------------------------------------------------------------------->
    def read(self):
        '''Reads the file'''
        print(self.fileContents)

    def write(self, sentence):
        '''Adds on the senence to the end of the file'''
        f = open(self.filePath, "w")
        f.write(str(self.fileContents) + str(sentence) + '\n')
        f.close()
        self.getFileContents()

    #<----------------------------------------------------------------------------------------------------->
    
    def replace(self, sentence, *line):
        '''Replaces the contents of the file or specific lines'''
        if line == ():
            self.clear()
            self.write(str(sentence))
            self.getFileContents()
        else:
            f = open(self.filePath, "r")
            listOfLines = f.read()
            test = listOfLines.split("\n")
            try:
                for x in line:
                    test[x - 1] = sentence
            except:
                raise Exception("Line number out of range.\n(Eg. list = [1, 2]\nprint(list[2]))")
            self.clear()
            for x in test:
                if x != "":
                    self.write(x)
        
    def clear(self, *line):
        '''Clears the file or specific line'''
        if line == ():
            f = open(self.filePath, "w").close()
            self.getFileContents()
        else:
            f = open(self.filePath, "r")
            listOfLines = f.read()
            test = listOfLines.split("\n")
            try:
                for x in line:
                    test[x - 1] = ""
            except:
                raise Exception("Line number out of range.\n(Eg. list = [1, 2]\nprint(list[2]))")
            self.clear()
            for x in test:
                if x != "":
                    self.write(x)

class jsonEditor:
    def __init__(self, filePath, notUsingJson = False, isAList = False):
        self.filePath = filePath
        self.fileType = None
        self.fileContents = None
        self.isAList = isAList
        self.getFileType(notUsingJson)
  
        self.getFileContents()
     
    def getFileType(self, notUsingJson = False): #Works
        '''Determines file type, no uses yet'''
        split = self.filePath.split('.')
        end = split[-1]
        self.fileType = end
        if self.fileType != 'json' and notUsingJson == False:
            raise Exception("Using jsonEditor on text files is not recommended due to curly braces and square braces.\nIf you still wish to proceed make notUsingJason = True.")

    def getFileContents(self):
        '''Gets or updates content of files, to not erase them'''
        try:
            self.fileContents = open(self.filePath, "r").read()
        except:
            self.fileContents = open(self.filePath, "w")
            self.fileContents = open(self.filePath, "r").read()
    
    def start(self):
        '''gets the beginning of the file ready for use'''
        self.write("{")
        if self.isAList:
            self.write("\t\"list\": [")
    
    def end(self):
        '''Gets the end of the fileready for use'''
        if self.isAList:
            self.write("\t]")
        self.write("}")

    #<----------------------------------------------------------------------------------------------------->
   
    def read(self):
        '''reads the contents of the file'''
        print(self.fileContents)

    def write(self, sentence):
        '''Writes to the file'''
        f = open(self.filePath, "w")
        f.write(str(self.fileContents) + str(sentence) + '\n')
        f.close()
        self.getFileContents() 
    
    #<----------------------------------------------------------------------------------------------------->
    
    def replace(self, sentence, *line):
        '''Replaces the contents of the file'''
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

    def createJsonDict(self, dictName, description, *content, lastInAList=False):
        '''Creates a dictionary to easily add to the file'''
        data = ""
        if self.isAList:
            data += ("\t{\n")
        data += "\t\"name\": \"" + str(dictName) + "\",\n\t\"description\": \"" + str(description) + "\","
        count = 1
        for x in content:
            data += "\n\t\"contents" + str(count) + "\": "
            if isinstance(x, list):
                data += str(x)
            else:
                data += "\"" + str(x) + "\""
            if count != len(content):
                data += ","
            data += "\t"
            count += 1
        
        if self.isAList:
            if lastInAList:
                data += "\n\t}"
            else:
                data += "\n\t},\n"
        
        data = data.replace("'", "\"")
        return data

import os

class fileManager:
    def __init__(self, filePath):
        self.filePath = filePath
        self.file_name = ""
        self.file_extension = ""
    
    def delete(self, filePath):
        os.remove(self.filePath + filePath)
    
    def createFile(self, name):
        open(self.filePath + "\\" + name, "w")

    def createFile(self, name):
        open(self.filePath + name, "w")
    
    def rename(self, filePath, newName):
        os.rename(self.filePath + filePath, newName)
    

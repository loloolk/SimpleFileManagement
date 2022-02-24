from fileManager.textEditor import textEditor

for x in range(1, 6):
    editor = textEditor("./exampleFolder/exampleFile" + str(x) + ".txt")
    editor.clear()
    editor.write(sentence = "This is a test sentence in file number " + str(x))
    editor.read()
    print(editor.fileContents)

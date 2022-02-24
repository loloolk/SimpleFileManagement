import fileManager

tList = ["hi", "hello", "hey", "sup", "good day", "greetings", "anyone here", "hallo"]
thList = ["Hello!", "Hey!", "Hi!", "Hey! What can I do for you?", "Howdy.", "Greetings.", "Hello."]
thiList = ["cya", "gtg", "goodbye", "Im leaving", "see you later", "see ya", "bye", "have a good day", "gotta go", "g2g"]
thisList = ["Bye!", "Sad to see you go :(", "Cya!", "Goodbye!", "Talk to you later!"]



editor = jsonEditor('./jsonExample.json', isAList=True)
editor.clear()
editor.start()

thisDict = editor.createJsonDict("Greeting", "Greeting section for chatbot", tList, thList)
testDict = editor.createJsonDict("Goodbye", "Goodbye section for chatbot", thiList, thisList, lastInAList=True)

editor.replace("lol", 1, 3, 5, 7, 9)
editor.write(thisDict)
editor.write(testDict)
editor.end()

#remove lastInList from createJsonDict
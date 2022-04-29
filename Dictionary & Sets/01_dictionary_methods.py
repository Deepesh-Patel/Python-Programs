myDict = {
"fast" : "In a quick manner",
"buddy" : "A programer",
"marks" : [1, 2, 5],
"anotherdict" : {'buddy' : 'player'},
1 : 2
}

#Dictionary Methods
print(list(myDict.keys()))     #Print the keys of the dictionary
print(myDict.values())          #Prints the values of the dictionary
print(myDict.items())           #Prints the (key, values) for all contents of the dictionary
print(myDict)

updateDict = {
"Cherish" : "Friend",
"Divya" : "Friend",
"Anup" : "Friend",
"Buddy" : "A Coder"
}

myDict.update(updateDict)      #Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

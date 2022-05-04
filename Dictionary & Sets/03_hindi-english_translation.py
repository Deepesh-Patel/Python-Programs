''' Write a python program to create a dictionary of
 hindi words with values as their english translation
  provide user with an option to look it up '''
  
myDict = {
    "Pankha": "Fan",
    "Dabba": "Box",
    "Vastu": "Item",
    "Kitab": "Book",
    "Insaan": "Human",
    "Ladka": "Boy"
}
print("The Options are:\n ", myDict.keys())
a = input("Enter the Hindi Word which you want to translate: ")
print("The meaning of your entered  word is: ", myDict.get(a))
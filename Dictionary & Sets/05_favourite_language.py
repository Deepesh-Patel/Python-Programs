''' Create an empty dictionary. Allow 4 friends to 
enter the favourite language as values and use 
keys as their names. Assume that the names are
unique. '''

favLang = {}

a = input("Enter your favourite language buddy: ")
b = input("Enter your favourite language chris: ")
c = input("Enter your favourite language clara: ")
d = input("Enter your favourite language jasmine:")

favLang['buddy'] = a
favLang['chris'] = b
favLang['clara'] = c
favLang['jasmine'] = d

print(favLang)
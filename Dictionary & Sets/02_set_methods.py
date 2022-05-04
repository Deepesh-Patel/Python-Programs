## Creating an empty set
b = set()
print(type(b))

## Adding values to an empty set
b.add(4)
b.add(4)
b.add(5)
b.add(5)    # Adding a value repeatedly does not changes the set
b.add((4, 5, 6))

## Accessing elements
#b.add({4:5})    # Cannot add list or dictionary to the sets
print(b)

## Length of the set
print(len(b))    # prints the length of this set

## Removal of an item
b.remove(5)    # removes 5 from set b
print(b)

print(b.pop())
print(b)
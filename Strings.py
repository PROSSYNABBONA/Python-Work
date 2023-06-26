#Strings
print("Fruits")
print('Fruits')

#Assign string to a variable
w="Fruits"
print(w)
#Multiline strings
q="""I am a Software engineer,year 2
learning recess
    """
print(q)
#Strings as arrays
a="Prossy"
print(a[1])#outputs r because it is at position 1

#Exercise 1:use the len()function to determine the length of the string
#Length of a string
b="Hello, Prossy!"
print(len(b))
#Execise 2:Give an example of using a for loop in a string
Person = "Prossy"
for x in Person:
  print(x)

#Exercise 3:Give an example of slicing in strings
#Slicing helps to return arange of using a slice syntax
w="Hello"
print(w[2:5])
#how to modify strings
a="Cars"
print(a.lower())
print(a.upper())

#Remove white space
b=" Afternoon "
print(b.strip())#removes spaces at the beginning and end
#String concantination
c="Class"
d="chair"
w=c+ " " + d
print(w)
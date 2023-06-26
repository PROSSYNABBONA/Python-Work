#Tuples are used to store items in a single variable,are oredered and uncharchangable
phones=("samsag","Ipone","Techno")
print(phones)
#Allow duplicate values
# phones=("samsag","Ipone","Techno","Iphone","Techo")

#1.Exercise:use the len() with this tuple example
print(len(phones))

#Tuples can have different datatypes
people=("Prossy","titi")
Numbers=(14,23,45,45)
print(type(Numbers))

#2.Exercise:Accesing tuples negative indexing,indecing
#Acess tuple items
print(phones[2])
print(phones[1])

#negative indexing,there is no zero,we start from -1
print(phones[-1])

#add items to a tuple(first convert the tuple to a list,then convert it back to the tuple)
Cars=("Rangerover","Benz","Ford")
z=list(Cars)
z.append("Tizi")
Cars=tuple(z)
print(Cars)

#Adding two tuples together
colors=("red","blue","orage")
color=("yellow",)#we put that comma for continuing
colors +=color
print(colors)#if u say print color it will only out put the yellow

#putting 2 tuples in one tuple
Newcolor=color+colors
print(Newcolor)

#looping through the tuples for loop
colors=("red","blue","orage")
for y in colors:
    print (y)
    
    #loop through tuples
    tuple = ("apple", "banana", "cherry")
for x in tuple:
  print(x)

#Lists are used to store multiple items
#Lists are ordered,changeable,and allows duplicate values
Afternoon=["Prossy","Tracy","Titi","Weti","Plau"]
print(Afternoon)

#Duplicates in Lists
Morning=["Prossy","Tracy","Titi","Prossy","Prossy","Titi"]
print(Morning)

#List Length
print(len(Morning))

#List Type
print(type(Afternoon))

#Acess List items
print(Afternoon[2])
print(Afternoon[1])

#negative indexing,there is no zero,we start from -1
print(Afternoon[-1])

Afternoon.append("Plau")
print(Afternoon)
#Acessing rage of items
print(Afternoon[3:5])
#this means all beginning items excluding that at position 4
print(Afternoon[:4])
 
print(Afternoon[1:])

#check if item exists
list = ["apple", "banana", "cherry"]
if "apple" in list:
  print("Yes, 'apple' is in the fruits list")


#Adding  element at a specific index
Afternoon.insert(0,"livi")
print(Afternoon)
#Removing list items
Afternoon.remove("livi")
print(Afternoon)
#remove list items using an index
Afternoon.pop(3)
#looing through list
list = ["apple", "banana", "cherry"]
for x in list:
  print(x)
  #copying lists
  thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#copying lists
list = ["apple", "banana", "cherry"]
mylist = list.copy()
print(mylist)

#joining lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#store multiple items  in the singlevariable
#unchangable
food={"rice","matooke","irish","potato"}
print(food)
#duplicates in sets
foodie={"rice","matooke","irish","potato","rice","rice"}
#Exercise:Length of the set,datatype,
# accessing items in a set,adding items ,add two sets together

#length
food={"rice","matooke","irish","potato"}
print(len(food))
#finding the datatype
print(type(food))
#accessing elements in a set
"""Acess List items,we cant access but we can
#loop through the srt items using a for loop or ask
if a specific value is present using the in keyword
"""
food={"rice","matooke","irish","potato"}
for x in food:
    print(x)
 #Checking if item is there
food={"rice","matooke","irish","potato"}
print("rice"in food)#outputs true

  #Adding items to the set
food={"rice","matooke","irish","potato"} 
food.add("Chicken")
print(food)

# #Adding multiple items we use update()
# food={"rice","matooke","irish","potato"}
# food.update(["kikomado","fish"])

#Joining two sets
set1={1,2,3,4}
set2={5,6}
set3=set1.union(set2)
print(set3)

Fruits = set(("apple", "banana", "cherry")) 
print(Fruits)

#removing sets items
Fruits = set(("apple", "banana", "cherry")) 
Fruits.remove("apple")
print(Fruits)

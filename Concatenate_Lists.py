# Write a function that concatenates two lists. [a,b,c], [1,2,3] → [a,b,c,1,2,3]

list_one = ["a", "b", "c"]
list_two = [1, 2, 3]

list_three = list_one + list_two #Python makes it extremely simple to concatenate two lists
print(list_three) #This will print the two concatenated lists

for x in list_two: #This is how it could also be done
  list_one.append(x) #This takes list one and concatenates the other elements onto it

print(list_one) #this will print list_one with its other elements


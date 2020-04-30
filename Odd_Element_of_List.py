# Write a function that returns the elements on odd positions in a list.
import random

number_list = []
MAX = 100

for i in range(0,MAX): #this will make a list with the MAX elements
    n = random.randint(1,MAX) #this sets a variable to the random integer 1 to MAX
    number_list.append(n) #this adds the integer to the list I create
print(number_list) #this will print the list
print("The elements of odd positions in a list")
for x in range(len(number_list)):
    if(x%2 == 1):
        print(number_list[x],end =" ")
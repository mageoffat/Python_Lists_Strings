# Write a function that checks whether an element occurs in a list.

import random

number_list = []
MAX = 100
element = random.randint(1,MAX)
is_found = False
print("We want to see if", element, "is found in this list")

for i in range(0,MAX): #this will make a list with the MAX elements
    n = random.randint(1,MAX) #this sets a variable to the random integer 1 to MAX
    number_list.append(n) #this adds the integer to the list I create
print(number_list) #this will print the list

for x in number_list: #this will go through and look at the elements of the list
    if x == element: #if the x is equal to the element I want to find
        print("yes", element, "is in list") # print yes it is in list
        is_found = True # raise the flag is_found to true   
        break #no need to traverse through the rest of the list
if(is_found == False): #if it was not found
    print("no", element, "is not in the list") #print it is not in the list


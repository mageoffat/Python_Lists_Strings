#Write function that reverses a list, preferably in place.
import random

number_list = []
MAX = 100


for i in range(0,MAX): #this will make a list with the MAX elements
    n = random.randint(1,MAX) #this sets a variable to the random integer 1 to MAX
    number_list.append(n) #this adds the integer to the list I create
print(number_list) #this will print the list

for x in range(len(number_list)//2): #this will go through half the elements of the 
    n = number_list[x] #saving the number 
    number_list[x] = number_list[MAX-x-1] # get the x element to become the last element -xth element
    number_list[MAX-x-1] = n #making the last element -x become whatever n is
print(number_list) #Prints the reversed list

for x in range(len(number_list)//2): #Python way to change it all
    number_list[x], number_list[MAX-x-1] = number_list[MAX-x-1], number_list[x] #this will reverse the list quickly
print(number_list) #Prints the reversed list
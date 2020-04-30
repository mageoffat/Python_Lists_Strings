# Write a function that returns the largest element in a list.
import random

number_list = []
MAX = 1000


for i in range(0,MAX): #this will make a list with the MAX elements
    n = random.randint(1,MAX) #this sets a variable to the random integer 1 to MAX
    number_list.append(n) #this adds the integer to the list I create
print(number_list) #this will print the list



largest_element = number_list[0] #this sets the largest_element to the first element of the list
for x in range(len(number_list)-1): #this will go through the elements by in the list with the length of the list
    if x < MAX: #This will make sure the numbers to not go out of bounds
        if number_list[x+1] > number_list[x] and largest_element < number_list[x+1]: #this tests to see if the number is larger
            largest_element = number_list[x+1] # this will make the largest_element become the bigger number
print(largest_element) #this prints the largest number



largest_element = number_list[0] #sets the largest_element to the first element of the list
for x in number_list: #Just using the x's as the next element in the list
    if x > largest_element: #checking to see if the element is greater than the largest_element
        largest_element = x #this will make the largest_element switch to the bigger number x
print(largest_element) #this prints the largest number of the list



print(max(number_list)) #this is an easy python way to find max of a number_list
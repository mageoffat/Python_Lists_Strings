#Write a function that computes the running total of a list.
import random
total = 0
add = 0
print("Do you want to enter your own list or sum up a random list")
user_input = input("Enter 1 (own) or enter 2 (random)")
try:
    val = int(user_input)
except ValueError:
    print("Enter 1 or 2")

if val == 1:
    print("If you do not enter a number it will end")
    while True:
        
        user_input = input("Which number do you want to sum?")
        
        try:
            add = int(user_input)
            total += add
            
        except ValueError:
            print(" ")
            break
    print(total)

    
elif val == 2:
    number_list = []
    MAX = 100
    for i in range(0,MAX): #this will make a list with the MAX elements
        n = random.randint(1,MAX) #this sets a variable to the random integer 1 to MAX
        number_list.append(n) #this adds the integer to the list I create
    print(number_list) #this will print the list
    print(sum(number_list))
    

else:
    print("Sorry that was not 1 or 2")

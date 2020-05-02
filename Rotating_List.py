# Write a function that rotates a list by k elements.
#  For example [1,2,3,4,5,6] rotated by two becomes [3,4,5,6,1,2].
#  Try solving this without creating a copy of the list.
#  How many swap or move operations do you need?

num_list = [1,2,3,4,5,6,7,8,9] # my numbered list
val = 0 # value

def rotation(num_list): #This is my rotation function 
    temp = 0 # temporaty variable
    temp = num_list[0] #this will set the temporary variable the first element of the list
    for x in range(1, len(num_list)): #This for goes through the rest of the numbers
        num_list[x-1] = num_list[x] #this will switch all the numbers by left
    num_list[len(num_list)-1] = temp # now make the last list element equal to temp
    

print("How much do you want the list to be rotated?") #print the question
val = input("Enter a number") #take input 
try: #see if it can be an int
    r = int(val) #make the r an int variable
except ValueError: # Error checker
    print("Sorry that is not a number") #print invalid

for i in range(0, r): #lets you rotate it as much as you want
    rotation(num_list) #Will call the rotation(num_list)

print(num_list) #will print the final num_list

#This one was difficult for me, even though looking at it now it seems fairly simple
# Write a function that takes a number and returns a list of its digits.
# So for 2342 it should return [2,3,4,2].

number = 2342
num_list = []
a = True

while(a):    
    temp = number%10
    number = number//10
    num_list.insert(0, temp)
    if (number == 0):
        a = False
        break

print(num_list)
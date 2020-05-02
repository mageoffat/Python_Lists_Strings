#  Write a function that computes the list of the first 100 Fibonacci numbers.
#  The first two Fibonacci numbers are 1 and 1.
#  The n+1-st Fibonacci number can be computed by adding the n-th and the n-1-th Fibonacci number.
#  The first few are therefore 1, 1, 1+1=2, 1+2=3, 2+3=5, 3+5=8.
import time
starttime = time.time()

fibonacci = []
val = 0


def Fib(val): #fibonacci sequence function (without recursion or dynamic programming)
    a = 0
    b = 1
    fibonacci.append(a)
    fibonacci.append(b)
    for x in range(2, val):
        c = a+b
        a = b
        b = c
        fibonacci.append(c)
    print(fibonacci)

print("What fibonacci do you want to know?") #print the question
val = input("Enter a number") #take input 
try: #see if it can be an int
    val = int(val) #make the r an int variable
except ValueError: # Error checker
    print("Sorry that is not a number") #print invalid

Fib(val) #will print the final num_list
print("time", time.time() - starttime)
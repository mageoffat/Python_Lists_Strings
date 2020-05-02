#  Write a function on_all that applies a function to every element of a list.
#  Use it to print the first twenty perfect squares.
#  The perfect squares can be found by multiplying each natural number with itself.
#  The first few perfect squares are 1*1= 1, 2*2=4, 3*3=9, 4*4=16.
#  Twelve for example is not a perfect square because there is no natural number m so that m*m=12.
#  (This question is tricky if your programming language makes it difficult to pass functions as arguments.)

from itertools import chain

const_max = 20
number_list = []
for x in range(1, const_max+1):
    number_list.append(x)

def perfect_squares(number_list):
    perfect_squares_list = []
    for i in range(len(number_list)):
        perfect_squares_list.append(number_list[i]*number_list[i])
    return perfect_squares_list
    
print(perfect_squares(number_list))

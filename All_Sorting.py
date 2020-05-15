#  Implement the following sorting algorithms:
#  Selection sort, Insertion sort, Merge sort, Quick sort, Stooge Sort.
#  Check Wikipedia for descriptions.
import random

number_list = []
MAX = 100

for i in range(0,MAX): #this will make a list with the MAX elements
    n = random.randint(1,MAX) #this sets a variable to the random integer 1 to MAX
    number_list.append(n) #this adds the integer to the list I create
print(number_list) #this will print the list


#Selection Sort
def selection_sort(number_list):
    for i in range(len(number_list)):
        new_index = i #this will help for the for loop after for iterating through
        for j in range(i+1,len(number_list)):
            if number_list[new_index] > number_list[j]:
                new_index = j
        number_list[i], number_list[new_index] = number_list[new_index], number_list[i]
    return(number_list)
print(selection_sort(number_list))
#
number_list = []
for i in range(0,MAX): #this will make a list with the MAX elements
    n = random.randint(1,MAX) #this sets a variable to the random integer 1 to MAX
    number_list.append(n) #this adds the integer to the list I create
print(number_list) #this will print the list
#

#Insertion Sort
def insertion_sort(number_list):
    for i in range(1,len(number_list)):
        temp = number_list[i]
        j = i-1
        while j >= 0 and temp < number_list[j]:
            number_list[j+1] = number_list[j]
            j -= 1
        number_list[j+1] = temp
    return(number_list)
print(insertion_sort(number_list))
#
number_list = []
for i in range(0,MAX): #this will make a list with the MAX elements
    n = random.randint(1,MAX) #this sets a variable to the random integer 1 to MAX
    number_list.append(n) #this adds the integer to the list I create
print(number_list) #this will print the list
#

#Merge Sort
def merge_sort(number_list): 
    if len(number_list) >1: 
        mid = len(number_list)//2 
        L = number_list[:mid]
        R = number_list[mid:]
  
        merge_sort(L) 
        merge_sort(R) 
  
        i = j = k = 0
          
      
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                number_list[k] = L[i] 
                i+=1
            else: 
                number_list[k] = R[j] 
                j+=1
            k+=1
          
       
        while i < len(L): 
            number_list[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            number_list[k] = R[j] 
            j+=1
            k+=1

print(number_list) 
merge_sort(number_list) 
print(number_list) 


#Quick Sort

#
number_list = []
for i in range(0,MAX): #this will make a list with the MAX elements
    n = random.randint(1,MAX) #this sets a variable to the random integer 1 to MAX
    number_list.append(n) #this adds the integer to the list I create
print(number_list) #this will print the list
#
  
# Function to do Quick sort 
def quick_sort(arr,low,high): 
    if low < high: 
        i = ( low-1 )         # index of smaller element 
        pivot = number_list[high]     # pivot 
    
        for j in range(low , high): 
    
            # If current element is smaller than the pivot 
            if   number_list[j] < pivot: 
            
                # increment index of smaller element 
                i = i+1 
                number_list[i],number_list[j] = number_list[j],number_list[i] 
    
        number_list[i+1],number_list[high] = number_list[high],number_list[i+1]  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = i+1
  
        # Separately sort elements before 
        # partition and after partition 
        quick_sort(number_list, low, pi-1) 
        quick_sort(number_list, pi+1, high) 
  
# Driver code to test above 
n = len(number_list) 
quick_sort(number_list,0,n-1) 
print(number_list)



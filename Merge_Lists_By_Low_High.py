# Write a function that merges two sorted lists into a new sorted list.
#  [1,4,6],[2,3,5] → [1,2,3,4,5,6].
#  You can do this quicker than concatenating them followed by a sort.

list_one = [1,4,6]
list_two = [5,7,8]

# list_one = [0,1,1,1,3,6,7,9,9]
# list_two = [1,4,6,6,6,6,8,8,9,9,9]

def low_high_list(list_one, list_two):
    i = 0
    j = 0
    list_three = []
    while(True):
        if i == len(list_one):
            while(j != len(list_two)):
                list_three.append(list_two[j])
                j += 1
            break
        elif j == len(list_two):
            while(i != len(list_one)):
                list_three.append(list_one[i])
                i += 1
            break
        if list_one[i] <= list_two[j]:
            list_three.append(list_one[i])
            i += 1
        elif list_one[i] > list_two[j]:
            list_three.append(list_two[j])
            j += 1

    return list_three

print(low_high_list(list_one, list_two))
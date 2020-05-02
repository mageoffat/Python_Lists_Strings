# Write a function that combines two lists by alternatingly taking elements.
#  e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3].

list_one = ["a", "b", "c", "d", "e", "f"]
list_two = [1, 2, 3, 4, 5]

def alternating_combination(list_one, list_two):
    list_three = []
    if (len(list_one) < len(list_two)):
        for i in range(len(list_one)):
            list_three.append(list_one[i])
            list_three.append(list_two[i])
    else:
        for i in range(len(list_two)):
            list_three.append(list_one[i])
            list_three.append(list_two[i])
    return list_three

print(alternating_combination(list_one, list_two))


#Write three functions that compute the sum of the numbers in a list:
#  using a for-loop, a while-loop and recursion.
#  (Subject to availability of these constructs in your language of choice.)
sum_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for_sum = 0
while_sum = 0
recursive_sum = 0
x = 0

def my_forloop_sum(sum_list):
  i = 0
  for_sum = 0
  for i in sum_list:
    for_sum += i
  return for_sum



def my_whileloop_sum(sum_list):
  while_sum = 0
  while True:
    while_sum = sum(sum_list)
    break
  return while_sum


def my_recursive_sum(sum_list):
  if(len(sum_list) == 1):
    return sum_list[0]
  return sum_list[0] + my_recursive_sum(sum_list[1:])
  

print(my_forloop_sum(sum_list))
print(my_whileloop_sum(sum_list))
print(my_recursive_sum(sum_list))

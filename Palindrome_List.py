#Write a function that tests whether a string is a palindrome.

word = input("Type a possible polindrome ")

is_palindrome = True
palindrome_list = list(word)
MAX = len(palindrome_list)
for x in range(len(palindrome_list)//2): #Python way to change it all
    if(palindrome_list[x] != palindrome_list[MAX-x-1]):  #this will reverse the list quickly
        is_palindrome = False
        print("Not a Palindrome")
if(is_palindrome):
    print("This is a Palindrome")

print(palindrome_list) #Prints the reversed list
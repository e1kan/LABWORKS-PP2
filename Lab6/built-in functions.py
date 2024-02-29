#1 - multiply all numbers in a list
str = input("Enter elements of list separated by space: ")
words = str.split()
answ = 1
for item in words:
    if item.isnumeric():
        answ *= int(item)
print(answ)

#2 -calculate the number of upper case letters and lower case letters
str = input("Enter a string: ")
low = 0
upp = 0
for char in str:
    if char.islower():
        low += 1
    elif char.isupper():
        upp += 1
print("Uppercase letters:", upp)
print("Lowercase letters:", low)

#3 - check a palindrome
str = input('Enter a string: ')
rev_str = str[::-1]
if bool(str == rev_str):
    print("Palindrome found!")
else:
    print("It is not a palindrome!")

#4 - invoke square root function after specific milliseconds
from time import sleep
from math import sqrt
num = int(input("Enter a number: "))
num_sqrt = sqrt(num)
milis = int(input("Enter miliseconds: "))
sleep(milis / 1000)
print("Square root of", num, "after", milis, "miliseconds is", num_sqrt)



#5 -  returns True if all elements of the tuple are true
def checkIfTrue(str):
    if not str:
        return False
    li = str.split()
    tup = tuple(li)
    for item in tup:
        if item == 'False' or item == '0':
            return False
    return True

str = input("Write elements of your tuple separated by space: ")
print(checkIfTrue(str))

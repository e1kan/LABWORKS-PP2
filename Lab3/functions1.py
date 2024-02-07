#1 - ounces to grams
def gramsToOunces(grams):
  ounces = 28.3495231 * grams
  return ounces

g = float(input("Enter the amount of grams: "))
print(g, "grams =", gramsToOunces(g), "ounces")





#2 - Farenheit to Celsius
def celsius(F):
  C = (5/9) * (F-32)
  print(F, "°F =", round(C, 1), "°C")

temper = int(input("Enter the temperature in Farenheit: "))
celsius(temper)





#3 - solve a puzzle
def solvePuzzle(numheads, numlegs):
  chicks = (4*numheads - numlegs) / 2
  rabbs = numheads - chicks
  print("Rabbits: ", int(rabbs))
  print("Chickens:", int(chicks))

legs = int(input("Enter the number of legs: "))
heads = int(input("Enter the number of heads: "))

solvePuzzle(heads, legs)





#4 - return only primes
def filterPrimes(str):
  numbers = [int(num) for num in str.split()]
  prime_numbers = []
  for x in numbers:
     isPrime = True
     if x < 2:
        continue
     for i in range(2, x):
        if x % i == 0:
          isPrime = False
          break
     if isPrime:
        prime_numbers.append(x)
  return prime_numbers

num = input("Enter integers separated by space: ")
print(filterPrimes(num))





#5 - all permutations of a string
from itertools import permutations
def strPermute(str):
  perm = permutations(str)
  for item in perm:
    print(''.join(item), end=', ')

s = input()
strPermute(s)





#6 - reverse string's words
def reverseWords(str):
    words = str.split()
    words.reverse()
    for item in words:
        print(item, end=' ')

s = input("Enter a string: ")
reverseWords(s)





#7 - does a list contain '33' in order?
def has_33(numlist):
    for i in range(len(numlist) - 1):
        if numlist[i] == 3 and numlist[i+1] == 3:
            return True
    return False

list1 = []
print("Enter 0 to stop:")
while True:
    x = int(input())
    list1.append(x)
    if x == 0:
        break

print(has_33(list1))





#8 - does a list contain '007' in order?
def spy_game(somelist):
    numnums = [int(num) for num in somelist.split()]
    zcount = 0
    scount = 0
    for num in numnums:
        if num == 0:
            zcount += 1
        elif num == 7 and zcount < 2:
            zcount = 0
        elif num == 7 and zcount >= 2:
            return "My-my, I think we have a spy!"
    return "Don't choose Spy in TF2..."

numlist = input("Enter numbers  separated by space: ")
print(spy_game(numlist))





#9 - volume of a sphere
import math
def sphere(radius):
  volume = 4 * math.pi * radius**3 / 3

r = int(input("Enter radius: "))
sphere(r)





#10 - take unique elements
def uniqueSearch(str):
   properList = [x for x in str.split()]
   ellist = []
   for item in properList:
      if item not in ellist:
         ellist.append(item)
   return ellist

li = input("Enter the list's elements separated by space: ")
print(uniqueSearch(li))




#11 - check palindrome
def isPalindrome(str):
   if len(str) == 1:
      return True
   else:
    for i in range(0, (len(str)) // 2):
      if str[i] != str[len(str) - i - 1]:
         return False
    return True

s = input("Enter a string: ")
print(isPalindrome(s))





#12 - make a historigram
def makeHistorigram(list):
  numlist = [int(x) for x in list.split()]
  for x in numlist:
    print('*'*x)

nums = input("Enter integers separated by space: ")
makeHistorigram(nums)





#13 - guess a number
import random
def guessNum():
  name = input("Hello! What is your name? \n")
  print("Well,", name + ", I am thinking of a number between 1 and 20.")
  answ = random.randint(1, 20)
  gcount = 0
  guess = int(input("Take a guess. \n"))
  while guess != answ:
    gcount += 1
    if (guess < answ):
      print("Your guess is too low.")
      guess = int(input("Take a guess. \n"))
    else:
      print("Your guess is too high.")
      guess = int(input("Take a guess. \n"))
  print("Good job,", name + "! You guessed my number in", gcount, "guesses!")

guessNum()

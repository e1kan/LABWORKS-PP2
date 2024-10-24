#..........examples:
#check if true
print(10 > 9)
print(10 == 9)
print(10 < 9)

#check using if else statements
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15
print(bool(x))
print(bool(y))

#returns True
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#returns False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
  def __len__(self): #__len__ will print out 0/False
    return 0
myobj = myclass()
print(bool(myobj))

def myFunction() :
  return True
print(myFunction())

def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")

x = 200
print(isinstance(x, int)) #checks if a var is of ... datatype




#..........exercises:
print(10 > 9) #True

print(10 == 9) #False

print(10 < 9) #False

print(bool("abc")) #True

print(bool(0)) #False
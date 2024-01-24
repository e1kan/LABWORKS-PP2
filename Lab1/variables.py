#..........examples:
x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(5)    # x will be '5'
y = int(3)    # y will be 3
z = float(55)  # z will be 55.0

x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
# is the same as
x = 'John'

a = "almond"
A = "Amy"
#A will not overwrite a

#legit names for variables
venom = "Carnage"
hell_no = "DOOM SLAYER IS HERE"
_my_bad = "Sorry man"
welcomeHome = "We were waiting"
GETOUTPLS = "HELP"
venom2 = "Pls, no sequels!"
#special cases:
myVariableName = "John" #Camel
MyVariableName = "John" #Pascal
my_variable_name = "John" #Snake

#NOT legit names for variables
2thehellandback = "Oh no..."
my-world-my-rules = "John"
I am inevitable = "thanos"

x, y, z = "Price", "Soap", "Gaz"
print(x)
print(y)
print(z)

x = y = z = "Soldier"
print(x)
print(y)
print(z)

zoopark = ["aardvark", "bison", "chicken"]
x, y, z = zoopark
print(x)
print(y)
print(z

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)

x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()

x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

#..........exercises:
carname = "Volvo"

x = 50

x = 5
y = 10
print(x + y)

x = 5
y = 10
z = x + y
print(z)

x, y, z = "Orange", "Banana", "Cherry"

x = y = z = "We are one"

def myfundc():
    global x
    x = "fantastic"

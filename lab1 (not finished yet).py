#!!!HOME & INTRO & GET STARTED:
#.............examples:
print("Hello, World!")

#.............exercises:
print("Hello, World!")





#!!!SYNTAX:
if 5 > 2:
#.............examples:
    print("YES") 
if 5 > 2:
 print("YES") 

 #.............exercises:
 if 5 > 2:
    print("YES") 





#!!!COMMENTS:
#.............examples:
#This is a comment
print("This is NOT a comment") #This is another comment

#print("This is also a comment")
print("Haha, this one isn't a comment")

#.............exercises:
#This is a comment
'''
This is a comment written in
more than just one line
'''





#!!!VARIABLES:
#.............examples:
x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Prototype" # x is now of type str
print(x)

x = str(6)    # x will be '6'
y = int(7)    # y will be 7
z = float(9)  # z will be 9.0

x = 5
y = "Crane"
print(type(x))
print(type(y))

x = "Poppy"
# is the same as
x = 'Poppy'

a = "Mary"
A = "Masha"
#A will not overwrite a

#legal names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
#illegal names:
2myvar = "John"
my-var = "John"
my var = "John"

#camel case:
myVarName = "Soap"
#pascal case:
MyVarName = "Ghost"
#snake case:
my_var_name = "Roach"

#assigning multiple values/variables:
x, y, z = "Francis", "Zoey", "Louis"
print(x)
print(y)
print(z)

x = y = z = "Bill"
print(x)
print(y)
print(z)

#unpacking a collection:
lyrics = ["I", "feel", "good"]
x, y, z = lyrics
print(x)
print(y)
print(z)

#.............exercises:
carname = "Volvo, not Bentley"

x = 50

x = 5
y = 10
print(x+y)

x = 5
y = 10
z = x + y
print(z)




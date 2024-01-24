#..........examples:
print("Hello")
print('Hello')

a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#printing out a char
a = "Hello, World!"
print(a[1]) #a

#looping through  string
for x in "banana":
  print(x) 

a = "Hello, World!"
print(len(a))

#check a word
txt = "The best things in life are free!"
print("free" in txt) #True

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt) #True

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#getting chars from 2 to 5 (2, 3, 4; 5 isn't included)
b = "Welcome Home"
print(b[2:5]) #lco

#getting chars from the start to 5
b = "Welcome Home" #welco
print(b[:5])
#getting chars from 2 to the end
b = "Welcome Home" #lcome Home
print(b[2:])

#getting chars starting from the right
b = "Hello, World!"
print(b[-5:-2]) #orl
c = "welcome guests"
print(c[-6:-1]) #guest

a = "Hello, World!"
print(a.upper()) #HELLO, WORLD!
a = "Hello, World!"
print(a.lower()) #hello, world!

#removes unecessary spaces
a = " Hello, World! "
print(a.strip()) #Hello, World!

a = "Hello, World!"
print(a.replace("H", "J")) #Jello, World!

a = "Hello, World!"
print(a.split(",")) #['Hello', ' World!']

a = "Hello"
b = "World"
c = a + b
print(c) #HelloWorld

a = "Hello"
b = "World"
c = a + " " + b
print(c) #Hello World

#combining strings with other data types
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age)) 
#My name is John, and I am 36

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) 
#I want 3 pieces of item 567 for 49.95 dollars.

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) 
#I want to pay 49.95 dollars for 3 pieces of item 567

#escape characters allow using quotes illegal characters
txt = "We are the so-called \"Vikings\" from the north."  

#All string methods return new values. They do not change the original string. 


#..........exercises:
x = "Hello World"
print(len(x))

txt = "Hello World"
x = txt[0]

txt = "Hello World"
x = txt[2:5]

txt = " Hello World "
x = txt.strip()

txt = "Hello World"
txt = txt.upper()

txt = "Hello World"
txt = txt.lower()

txt = "Hello World"
txt = txt.replace("H", "J")

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
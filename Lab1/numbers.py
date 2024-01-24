#..........examples:
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))

#int examples:
x = 1
y = 35656222554887711
z = -3255522

#float examples:
x = 1.10
y = 1.0
z = -35.59
a = 35e3
b = 12E4
c = -87.7e100

#complex examples:
x = 3+5j
y = 5j
z = -5j

#conversion:
x = 1    # int
y = 2.8  # float
z = 1j   # complex
a = float(x) #1.0
b = int(y) #2
c = complex(x) #1 + 0j

#random number from a range
import random
print(random.randrange(1, 1000))

#..........exercises:
x = 5
x = float(x)

x = 5.5
x = int(x)

x = 5
x = complex(x)

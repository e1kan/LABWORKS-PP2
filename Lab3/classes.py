#1 - getstring and printstring
class TrickyString:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())

s = TrickyString()
s.getString()
s.printString()


#2 - shape and square
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

x = int(input())
a = Square(x)
print(a.area())


#3 - rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

b = Rectangle(4, 5)
print(b.area())

#4 - point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("Coordinates: ({}, {})".format(self.x, self.y))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance

#5 - bank account
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount} successfully.")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")

my_account = Account("Mercer", 1000)
my_account.deposit(500)
my_account.deposit(100)
my_account.withdraw(200)
my_account.withdraw(1500)

#6 - using lambda
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = []
primes = list(filter(lambda x: isPrime(x), numbers))
print(primes)

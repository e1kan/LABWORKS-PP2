#1 - all squares up to  n
n = int(input("Print all squares up to: "))
generator = (x**2 for x in range(0,n))
for i in generator:
    print(i)

#2 - all even nums from 0 to n
n = int(input("Print all even numbers up to: "))
generator = (i for i in range(0,n+1) if i % 2 == 0)
for i in generator:
    print(i)


#3 - nums from 0 and n divisible by 3 and 4 (func)
def ThreeFourGenerator(n):
    i = 0
    while i < n:
        if i % 3 == 0 and i % 4 == 0:
            yield i
        i += 1

n = int(input())
for i in ThreeFourGenerator(n):
    print(i)



#4 - yield the square of all nums from (a) to (b) (func)
def yieldSquaresGenerator(a, b):
    while a <= b:
        yield a**2
        a = a + 1

start = int(input())
end = int(input())
for x in yieldSquaresGenerator(start, end):
    print(x)

#5 - all nums from (n) to 0
n = int(input())
generator = (i for i in reversed(range(0, n)))
for i in generator:
    print(i)

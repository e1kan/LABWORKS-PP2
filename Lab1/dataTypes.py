#..........examples:

x = 5
print(type(x))

x = str("Hello World")	#str	
x = int(20)	#int	
x = float(20.5)	#float	
x = complex(1j)	#complex	
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	#range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	#bool	
x = b"Hello"	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview	
x = None	#NoneType

#specifying a type examples
x = list(("apple", "banana", "cherry"))	#list	
x = tuple(("apple", "banana", "cherry"))	#tuple	
x = dict(name="John", age=36)	#dict	
x = set(("apple", "banana", "cherry"))	#set	
x = frozenset(("apple", "banana", "cherry"))	#frozenset	
x = bool(5)	#bool	
x = bytes(5)	#bytes	
x = memoryview(bytes(5))	#memoryview	
x = None	#NoneType

#..........exercises:
x = 5
print(type(x)) #class 'int'


x = "Hello World"
print(type(x)) #class 'str'

x = 20.5
print(type(x)) #class 'float'

x = ["apple", "banana", "cherry"]
print(type(x)) #class 'list'

x = ("apple", "banana", "cherry")
print(type(x))  #class 'tuple'

x = {"name" : "John", "age" : 36}
print(type(x)) #class 'dict'

x = True
print(type(x)) #class 'bool'
#..........examples:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) #apple, banana
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) #apple

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(6):
  print(x) #0-5, range() by default starts with 0

for x in range(2, 6):
  print(x) #2-5

for x in range(2, 30, 3):
  print(x) #2, 5, 8, ..., 26, 29; increasing by 3

for x in range(6):
  print(x)
else:
  print("Finally finished!")

#If the loop breaks, the else block is not executed
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#a nested loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

for x in [0, 1, 2]:
  pass


#..........exercises:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#pass when banana encountered
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
   continue
  print(x)

for x in range(6):
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
   break
  print(x)
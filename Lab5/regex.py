#1 - match a string that has 'a' followed by 0 or more 'b's
#example: ab, a, abb, ba, dcab - match, abbd, abc - don't match
import re #re is a module
txt = input()
pattern = 'a(b*)'
if re.search(pattern, txt):
    print("Found a match!")
else:
    print("No match")


#2 - match a string that has 'a' followed by 2 or 3 'b's
#example: abb, abb, cabb - match, ab, dac, babbbb - don't match
import re
txt = input()
pattern = 'ab{2,3}'
if re.search(pattern, txt):
    print("Found a match!")
else:
    print("No match")


#3 - find the sequences of lowercase letters joined with a underscore
#example: 'hello_world' - match, 'hello*world', 'hELLO_WORLD' - don't match
import re
txt = input()
pattern = r'\b[a-z]+(?:_[a-z]+)+\b'
x = re.findall(pattern, txt)
print(x)


#4 - find the sequences of one upper case letter followed by lower case letters
#example: 'A_world', 'B_hi_me - match, 'A_WORLD', 'A_world_*world' - don't match
import re
txt = input()
pattern = r'\b[A-Z]{1}(?:_[a-z]+)+\b'
x = re.findall(pattern, txt)
print(x)


#5 - match a string that has an 'a' followed by anything, ending in 'b'
#example: 'acb, a_worldb', 'aB_*56hi_me!b - match, 'Ab', 'aA_world_*world_B' - don't match
import re
txt = input()
pattern = '^a.*?b$'
if re.search(pattern, txt):
    print("Found a match!")
else:
    print("No match")


#6 - replace all occurrences of space, comma, or dot with a colon
#example: Hello, it is me. i am here ---> Hello::it:is:me::i:am:here
import re
txt = input()
x = re.sub('[ ,.]', ':', txt)
print(x)


#7 - convert snake case string to camel case string
#example: hello_world_hi -> helloWorldHi
import re
txt = input()
pattern = '_([a-z])'
answ = re.sub(pattern,  lambda x: x.group(1).upper(), txt)
print(answ)


#8- split a string at uppercase letters
#example: HelloWorld --> ['Hello', 'World']
import re
txt = input()
x = re.findall('[A-Z][^A-Z]*', txt)
print(x)


#9- insert spaces between words starting with capital letters
#example: HelloWorld! ---> Hello World
import re
txt = input()
x = re.sub(r"(\w)([A-Z])", r"\1 \2", txt)
print(x)


#10- convert a given camel case string to snake case
#example: helloWorld ---> hello_world
import re
txt = input()
x = re.sub(r'([a-z])([A-Z])', r'\1_\2', txt).lower()
print(x)

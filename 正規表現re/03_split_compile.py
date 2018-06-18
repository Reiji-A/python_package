import re

s = "My name is ... Mike"
print(s.split())

p = re.compile(r"\W+")
print(p.split(s))

p = re.compile("(blue|white|red)")
print(p.sub("color","blue socks and red shoes"))
print(p.sub("color","blue socks and red shoes",count=1))
print(p.subn("color","blue socks and red shoes"))
p_1 = p.subn("color","blue socks and red shoes")
p_1[1]

def hexrepl(match):
    value = int(match.group())
    return hex(value)

p = re.compile(r"\d")
print(p.sub(hexrepl,"12345 55 11 test test2"))

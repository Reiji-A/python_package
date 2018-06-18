import re

# Greedy
s = "<html><head><title>Title</title></head></html>"

print(re.search(r"<title>.*</title>",s))
print(re.match(r"<.*>",s))

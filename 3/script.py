from collections import Counter
import re

x = ""
with open("test", "r") as f:
	for l in f:
			# print(l)
		x += l.strip()
		
s = ""
result = re.findall(r"[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", x)
# for i in result:
# 	s += i[3]
print(''.join(result))
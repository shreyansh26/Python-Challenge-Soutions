from collections import Counter

with open("file2", "r") as f:
	x = f.read()

c = Counter(x)
print(c.most_common())
from collections import Counter

with open("2.html", "r") as f:
	x = f.read()

c = Counter(x)
print(c.most_common())
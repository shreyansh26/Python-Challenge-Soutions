import pickle

with open("banner.p", "rb") as f:
	x = pickle.load(f)

# print(x)
# Tuple of chars

for lt in x:
	print(''.join([k*v for (k, v) in lt]))
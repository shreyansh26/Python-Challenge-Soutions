import requests

link = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
s = "12345"
i = 0
while(i<400):
	r = requests.get(link+s)
	s = r.text
	print(r.text)
	s = s.split()[-1]
	i += 1
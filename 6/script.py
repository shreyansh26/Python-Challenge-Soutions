# Open channel.zip :-|

import os, zipfile
import re

f = zipfile.ZipFile("channel.zip")
# os.chdir('./files')
s = '90052'
comments = []

while(1):
	content = f.read(s+'.txt').decode('utf-8')
	print(content)
	comments.append(f.getinfo(s+'.txt').comment.decode('utf-8'))
	nextnum = re.search(r"[A-Za-z ]+(\d+)", content)
	if nextnum == None:
		break
	s = nextnum.group(1)


print(''.join(comments))
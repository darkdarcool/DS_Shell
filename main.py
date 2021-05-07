from _read import read
from _code import code
while (True):
	l_data = input("$) ")
	l_data = l_data.split(" ")
	if ("read" in l_data):
		read(l_data)
	elif ("code" in l_data):
		code(l_data)
	else:
		print("Unkown command.")

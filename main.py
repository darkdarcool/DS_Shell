from _read import read
from _code import code
while (True):
	try:
		l_data = input("$) ")
		l_data = l_data.split(" ")
		f = len(l_data)
		if ("read" in l_data):
			read(l_data)
		elif ("code" in l_data):
			code(l_data)
		elif (l_data[0:f] == "" or l_data[0:f] == " "):
			None
		else:
			print("Unknown Command")
	except KeyboardInterrupt:
		print("If you would like to exit")

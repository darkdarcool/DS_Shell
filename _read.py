import os
def read(data):
	e = len(data)
	for i in range(e):
		isFile = open("main.py")
		isFile.close()
		try:
			if (data[i] == "read"):
				f = i + 1
				if (data[f] == "" or data[f] == " "):
					print("Expected file but got none")
					return None
				try:
					isFile = open(f"{data[f]}", 'r')
				
				except:
					isFile.close()
					print(f"{data[f]} is not an existing file")
					return None
				isFile.close()
				os.system("cat " + data[f])
                     print()

			else:
				pass
		except:
			pass

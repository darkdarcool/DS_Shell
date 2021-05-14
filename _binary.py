import os
def binary(data):
	e = len(data)
	for i in range(e):
		if (data[i] == "binary"):
			file = i + 1
			try:
				data[file]
			except:
				print("File was Expected")
				return None
			if (data[file] == "--mono"):
				file = file + 1
				try:
					isFile = open(data[file], 'r')
					isFile.close
				except:
					print("File was Expected")
					return None
				os.system(f"mono {data[file]}")
			else:
				try:
					isFile = open(data[file], 'r')
					isFile.close()
				except:
					print("File does not exist")
					return None
				os.system(f"./{data[file]}")
		

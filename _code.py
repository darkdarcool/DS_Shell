import os
def code(data):
	e = len(data)
	for i in range(e):
		iscodefile = open("main.py")
		iscodefile.close()
		if (data[i] == "code"):
			lang = i + 1
			if (data[lang] == "" or data[lang] == " "):
				print("Expected lang")
				return None 
			file = lang + 1 
			if (data[file] == "" or data[file] == " "):
				print("Expected file but got none")
				return None
			try:
				iscodefile = open(f"{data[file]}", 'r')
			except:
				iscodefile.close()
				print(f"{data[file]} is not a file.")
				return None 
			iscodefile.close()
			os.system(f"{data[lang]} {data[file]}")
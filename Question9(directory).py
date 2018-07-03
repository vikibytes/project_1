directory = {"Jane Doe":"+27 555 5367", "John Smith":"+27 555 6254", "Bob Stone":"+27 555 5689"}
directory["Jane Doe"] = "+27 555 1024"
directory["Anna Cooper"] = "+27 555 3237"
try :
	print("Bob's number is :", directory["Bob Stone"])
except :
	print("None")
print(directory.keys())
print(directory.values())
	
		
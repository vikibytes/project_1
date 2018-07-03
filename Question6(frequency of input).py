f = input("Please enter your sentence ")
a = f.split()
j = set(a)
for i in j:
		print(i, " : ", a.count(i))
		
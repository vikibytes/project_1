ok = False
while not ok:	
	a = input("Enter the number")
	try:
		a = int(a)
		b = a + a*a + a*a*a + a*a*a*a
		print("The required sum is ", b)
		ok = True
	except:
		print("Please enter a valid integer")

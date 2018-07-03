print("We are starting the question now ")
a = tuple([1, 1, 2, 3, 3])
b = list(a)
print("The length of the given list is ", len(b))
c = set(b)
print("The length of the given set is ", len(c))
d = list(c)
print("The length of the given list is ", len(d))
e = list(range(1, 11))
print("The lsit you created with range 1-10 is : ", e)
directory = {"Jane Doe":"+27 5555367", "John Smith":"+27 555 6254", "Bob Stone":"+27 555 5689"}
t = [("Jane Doe", "+27 5555367"), ("John Smith", "+27 555 6254"), ("Bob Stone", "+27 555 5689")]
v = directory.values()
k = directory.keys()
s = "antidisestablishmentarianism"
s1 = list(s)
s1.sort()
print(s1)
print("The output type is a list")
s2 = ""
for i in s1 :
	s2 = s2 + i
print(s2)
s3 = "the quick brown fox jumped over the lazy dog"
w = s3.split()
print(w)





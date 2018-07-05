#accpets a sequence of whitespace separated word and print afterremoving duplicate and sorting them in alphanumerically
s = input("Enter your sentence pleasse \n")
list_1 = s.split()
list_2 = list(set(list_1))
list_2.sort()
print(list_2)
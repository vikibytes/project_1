#https://www.hackerrank.com/contests/cosmocode-2-0/challenges/albert-desmonds-evil-lab
import itertools
a = input() #4 3 3
b = a.split()
no_of_floors = int(b[0])
typesoffloors = int(b[1])
listsize = []
for i in range(0, typesoffloors):
	listsize = listsize + [i+1]	
maxrepeat = int(b[2])
elements = listsize*maxrepeat
elements.sort()
c = list(itertools.combinations(elements, no_of_floors))
print(len(set(c)))
	
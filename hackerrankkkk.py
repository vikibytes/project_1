#https://www.hackerrank.com/contests/cosmocode-2-0/challenges/dinner-time
import itertools
no_of_avengers = int(input())
secretcode = []
for i in range(0, no_of_avengers):
	secretcode = secretcode + [input()]	
count = 0	
c = list(itertools.combinations(secretcode, 2))
print(c)
for j in range(0,  len(secretcode)):
	try :
		b = set(c[j][0]+c[j][1])
		print(b)
		b.remove('1')
		b.remove('2')
		b.remove('3')
		b.remove('4')
		b.remove('5')
		b.remove('6')
		b.remove('7')
		b.remove('8')
		b.remove('9')
		b.remove('0')
		count = count + 1
	except :
		pass
print(count)
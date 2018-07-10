#https://www.hackerrank.com/contests/cosmocode-2-0/challenges/superpower-mania
import sys
a = []
a.append(sys.stdin.readlines())
# print(a)
a = a[0]
days = int(a[0])
prices = a[1]
prices = [int(i) for i in prices.split()]
rev_prices = list(reversed(prices))
cases = int(a[2])
tests = [int(i) for i in a[3:]]
days=len(prices)
for i in tests:
    try:
        print(days - rev_prices.index(i))
    except:
        print(-1)
	

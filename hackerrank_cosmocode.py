#https://www.hackerrank.com/contests/cosmocode-2-0/challenges/albert-desmonds-evil-lab

no_of_days = int(input())
cost = input()
costlist = cost.split()
no_of_players = int(input())
player_cost = []
for i in range(0, no_of_players):
	player_cost = player_cost + [int(input())]
for i in player_cost:
	for j in range(len(costlist)-1, -1, -1):
		if i >= int(costlist[j]) :
			count = 0
			count = j+1
			break
		else:
			pass
	try :		
		print(int(count))
		count = 's'	
	except :
		print('-1')	
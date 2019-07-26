import math
number_of_rounds = int(input())
i = 0
j = 0
inp = []
all_lead =[]
score1 = 0
score2 = 0
maxx = 0
winner = []
for i in range(number_of_rounds):
	inp = input().split()
	score1 = score1 + int(inp[0])
	score2 = score2 + int(inp[1])
	difference = score2-score1
	lead = math.sqrt(difference*difference)
	all_lead.append(lead)
	if score1>score2 :
		winner.append(1)
	else :
		winner.append(2)
	i += 1
	
for j in range(number_of_rounds):
	num = int(all_lead[j])
	if num > maxx :
		maxx = num
		winner_var = j
	else: 
		num = 0
final_winner = int(winner[winner_var])
print(final_winner ,"%d"%maxx)
j+=1

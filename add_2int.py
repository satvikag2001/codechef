number_of_cases = int(input())
#number of cases
i =1
total = []
while i <= number_of_cases :
	inp = 0
	inp = input().split()
	sum = int(inp[0])+int(inp[1])
	total.append(sum)
	i += 1
#add all sums to a list 'total'

i=0

while i <= number_of_cases-1:
	print(int(total[i]))
	i += 1

#display all elements of total line by line as integers







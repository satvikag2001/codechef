number_of_cases = int(input())
i = 0
inp = []
all_remainder = []
for i in range(number_of_cases):
	inp = input().split()
	num1 = int(inp[0])
	num2 = int(inp[1])
	remainder = num1%num2
	all_remainder.append(remainder)
	i += 1
j = 0
for j in range(number_of_cases):
	print("%d"%all_remainder[j])
	j += 1
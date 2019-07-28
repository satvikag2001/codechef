import math
number_of_cases = int(input())
i = 0
for i in range(number_of_cases):
	number = int(input())
	root = math.sqrt(number)
	root = int(root + 0.5)
	print(root, "\n")
number_of_cases = int(input())
i = 0
j = 1
k = 0
factors = []
sorted_factors = []
for i in range(number_of_cases):
	number_of_cupcakes = int(input())
	i += 1
	while j <= number_of_cupcakes:
		remainder = (number_of_cupcakes +1)%j
		if remainder == 0:
			factors.append(j)
		else:
			remainder = 0
	sorted_factors=sorted(factors)
	maxx = sorted_factors[-1]
	all_maxx.append(max)
	j += 1
for k in range(number_of_cases)	:
	print("%d"%all_maxx[k])
	k += 1
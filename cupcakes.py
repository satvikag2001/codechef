number_of_cases = int(input())
i = 0

k = 0

all_maxx=[]
for i in range(number_of_cases):
	number_of_cupcakes = int(input())
	if number_of_cupcakes%2 == 0:
		maxx = (number_of_cupcakes + 2)/2
	else:
		maxx = (number_of_cupcakes +1)/2
	all_maxx.append(maxx)
for k in range(number_of_cases)	:
	print("%d"%(all_maxx[k]))
	k += 1
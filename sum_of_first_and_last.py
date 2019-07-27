import math
number_of_cases = int(input())
i = 0#loop variable
all_sum=[]#list of sums
summ = 0#sum that resets every loop
a=0#loop variable
while i<number_of_cases:
	number =  int(input())
	number_of_digits = math.log(number,10) + 1
	nod=int(number_of_digits)#shows error unless int defined
	for a in range(2):
		digit=number%10
		digit=int(digit)#shows error unless int defined
		summ = summ + digit

		print("%d{%d}%d"%(digit, summ,number))
		number = (number )/int(math.pow(nod-1,10))
		print(math.pow(10,nod-1))
		print("%d,%d"%(number,nod))
		#last digit added to sum and then removed.
		number=int(number)#shows error unless int defined
		a += 1

	all_sum.append(summ)#list with all sums

	summ=0	
	i = i+1
j=0#loop variable
for j in range(number_of_cases):
	print("%d"%all_sum[j])
	j += 1

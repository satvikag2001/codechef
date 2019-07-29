import math
number_of_cases = int(input())
i = 0#loop variable
all_counts=[]#list of sums
count = 0#count that resets every loop
a=0#loop variable
while i<number_of_cases:
	number =  int(input())
	number_of_digits = math.log(number,10) + 1
	nod=int(number_of_digits)#shows error unless int defined
	if number <= 9:
		if number==4:
			all_counts.append(1)
		
			all_counts.append(0)
	else:
		
		for a in range(nod):
			digit=number%10
			digit=int(digit)#shows error unless int defined
			if digit == 4:
				count += 1
			else:
				count = count
			number = (number )/10
			#last digit added to sum and then removed.
			number=int(number)#shows error unless int defined
			a += 1
		all_counts.append(count)#list with all sums

	count=0	
	i = i+1
j=0#loop variable
for j in range(number_of_cases):
	print("%d"%all_counts[j])
	j += 1

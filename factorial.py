number_of_cases = int(input())
#number of cases
i = 0
a = 1
factorial = 1
#a is the number used in loop for factorial
while i in range( number_of_cases) :
	number=int(input())
	a=1
	while a <= number:
		factorial=factorial*a
		a +=1
	print(factorial)
	factorial=1
	i += 1
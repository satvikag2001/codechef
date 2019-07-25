number_of_cases = int(input())
i=0
pr = 0
all_numbers = []
#defining loop variables,lists and number of cases
for i in range(number_of_cases):
#adding input to a list
		number = int(input())
		all_numbers.append(number)
		i += 1
sorted_numbers = sorted(all_numbers)
#sorting the list

#from to number of cases is 1 extra
while pr  <= number_of_cases -1:
		print("%d"%(sorted_numbers[pr]))
		pr += 1
		


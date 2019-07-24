inp = input().split()
number_of_cases = int(inp[0])
divisor =  int(inp[1])
#taking input in a list
i = 0
count = 0
#making a loop to take input,divide and increase count
while i<number_of_cases:
	case =  int(input())
	if case%divisor == 0:
		count = count + 1
	else:
		count = count
	i=i+1
#once counting is complete print it
print("%d"%count)
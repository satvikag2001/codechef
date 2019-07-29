number_of_cases = int(input())
i = 0
for i in range(number_of_cases):
	
	inp = input().split()
	a = int(inp[0])
	b = int(inp[1])
	c = int(inp[2])
	if (a>b and a>c):
		if b>c:
			print(b)
		else :
			print(c)
	elif (b>a and b>c):
		if a>c:
			print(a)
		else :
			print(c)
	elif (c>b and c>a):
		if b>a:
			print(b)
		else :
			print(a)		
	
	i += 1
	
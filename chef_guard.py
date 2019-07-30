number_of_cases = int(input())
for i in range(number_of_cases):
	inp = input().split()
	a = int(inp[0])
	b = int(inp[1])
	if a>b:
		minn = a
	else:
		minn = b
	maxx = a+b
	print("%d %d"%(minn,maxx))
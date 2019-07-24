inp = input().split()
#making a list and adding input in it
x = int(inp[0])
y = float(inp[1])
#dumping input as int and float
if x + 0.50 <= y :
#withdrawal should be less than balance after bank fees deducted	
	if x%5 == 0:
		print(" %0.2f " % (y - x - 0.50))
	else :
		print(" %0.2f " % y)
		#withdrwal must be multiple of 5
else :
	print(" %0.2f " % y)
     
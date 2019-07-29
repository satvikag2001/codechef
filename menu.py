all_num = []
p= int(input())

def divide(number):
	for i in range(12):
		if number != 0:	
			number = number/pow(2,i)
			rem = number%pow(2,i)
			print("[%d]"%number)
			if number == 1:
				all_num.append(i)
				number = rem
				divide(number)
				print("%d"%all_num[0,1])
				break
			else:
				continue
		else:
			print("%d"%all_num[0,1])
		i += 1
divide(p)

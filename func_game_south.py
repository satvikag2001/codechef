from sys import exit
import func_extra
prompt = ">>>>"

def south():
	print("You have entered the castle of DOOM ,from its rear end")
	print("It is dark and faint sounds of screaming can be heard.")
	print("you are absoulutely defenceless so like every sane peron you walk down the dusty corridor taking in")
	print("all that you can see.you make out 3 doors .What do you do")
	print("#hint:try typing 'open door 1' or 'go back'")

	S_dr_1_list = ['open door 1', 'open door 2', 'open door 3', 'go out']
	S_dr_1 = input(prompt)
	while S_dr_1 not in S_dr_1_list:
 		print("You cannot do that ")
 		S_dr_1 = input(prompt)
	if S_dr_1 =="open door 1":
 		S_dr_1_1()
	elif S_dr_1 =="open door 2":
 		S_dr_1_2()
	elif S_dr_1 =="open door 3":
 		S_dr_2_3()
	else :
 		func_extra.dead("the grim reaper was waiting for u outside.he drank your soul\n")

def S_dr_1_1() :
	print(" There is a giant cat here eating a cheese cake. What do you do?")
	print("1. Take the cake .")
	print("2' Scream at the bear.")
	
	cat = input(prompt)

	if cat == "take the cake" or cat == "1":
		func_extra.dead("The bear eats off yours face. Good job!")
	elif cat=="2"or cat == "scream at the bear":
		func_extra.dead("the bear eats your legs off. Good job!")
	else :
		print("Well doing %s is probably better. The bear ran away \n You win"%cat)
		print("there is nothing else to do ")
		S_dr_1_1 = input()
def S_dr_1_1() :
	print("good")
	func_extra.play_again()
def S_dr_1_1() :
	print("good")
	func_extra.play_again()



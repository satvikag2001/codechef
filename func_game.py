from sys import exit
prompt = ">>>>"
def play_again():
	print("do you want to play again")
	play_again = input(prompt)
	while play_again != "yes" and play_again != "no":
		print("please enter 'yes' or 'no'")
		play_again=input(prompt)
	if play_again == "yes":
		south()
	else :
		exit(0)
def south():
	print("You have entered the castle of DOOM ,from its rear end")
	print("It is dark and faint sounds of screaming can be heard.")
	print("you are absoulutely defenceless so like every sane peron you walk down the dusty corridor taking in")
	print("all that you can see.you make out 3 doors .What do you do")
	print("#hint:try typing 'open door 1' or 'go back'")

	S_dr_1_list = ['open door 1', 'open door 2', 'open door 3', 'go back']
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
 		dead("the grim reaper was waiting for u outside.he drank your soul\n")

def S_dr_1_1() :
	print("good")
	play_again()
def S_dr_1_1() :
	print("good")
	play_again()
def S_dr_1_1() :
	print("good")
	play_again()
def dead(reason_of_death):
	print(reason_of_death,"You lose")
	play_again()

south()
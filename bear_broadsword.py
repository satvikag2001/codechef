from sys import exit
from random import randint
prompt = ">>>>"
def play_again():
	print("do you want to play again")
	play_again = input(prompt)
	while play_again != "yes" and play_again != "no":
		print("please enter 'yes' or 'no'")
		play_again=input(prompt)
	if play_again == "yes":
		runner(ROOMS, 'princess_lives_here')
	else :
		exit(1)
def death() :
	quips = ["You died. You kinda suck. ",
			 "Your mama would be proud. If she was smarter",
			 "such a loser",
			 "I have a small puppy thats better at this."]
	print (quips[randint(0,len(quips)-1)])
	play_again()
	
def princess_lives_here() :
	print("You see a beatiful Princess with a shiny crown")
	print("She offers you some cake.")

	eat_it = input(prompt)

	if eat_it == "eat it" :
		print("You explode like a pinata full of frogs")
		print("THe Princess cakcles and eats the frogs")
		return 'death'

	elif eat_it == "do not eat it":
		print("She throws the cake at you and it cuts off your head.")
		print("The last thing you see is her munching on your torso")
		return'death'
	elif eat_it == "make her eat it":
		print("The Princess smiles as you cram the cake in her mouth")
		print("Then she smiles and cries and thanks you for saving her.")
		print("She points to a tiny door and says,'The koi need cake too.'")
		print("She gives you the very last bit of cake and shoves you in")
		return 'gold_koi_pond'

	else:
		print("The princess looks at you confused and just points at the cake.")
		return('princess_lives_here')
def gold_koi_pond() :
	print("There is a garden with a koi pond in the centre.")
	print("You walk close and see a massive fin poke out.")
	print("You peek in and a creepy looking huge Koi stares at you")
	print("It opens its mouth waiting for food.")

	feed_it = input(prompt)

	if feed_it == "feed it":
		print("The Koi jumps up and rather than eating the cake, eats your arm.")
		print("You fall in and the Koi shrugs and then eats you.")
		print("You are then pooped out sometime later.")
		return 'death'

	elif feed_it == "do not feed it":
		print("The Koi grimaces, then trashes arounds for a second")
		print("It rushes to the other end of the pond, braces against the wall")
		print("then it *lunges* out of the water, up in the air and over your")
		print("entire body, cake and all.")
		print("You are then pooped out a week later.")
		return 'death'

	elif feed_it == "throw it in" :
		print("The Koi wiggled ,then leaps into the air to eat the cake.")
		print("You can see it's happy, it then grunts, thrashes ...")
		print("and finally rolls over and poops a magic diamond into the air")
		print("at your feet.")

		return 'bear_with_sword'

	else :
		print("The Koi gets annoyed and wiggles a bit.")
		return 'gold_koi_pond'

def bear_with_sword() :
	print("Puzzled, you are about to pick up the fish poop diamond when")
	print("a bear bearing a load bearing sword walks in.")
	print("Hey! That\' my diamond! Where\'d you get that")
	print("It holds it paws out and looks at you.")

	give_it = input(prompt)

	if give_it == "give it":
		print("The bear swipes at your hand to grab the diamond and")
		print("rips your hand off in the process. It then looks at")
		print('your bloody stump,"oh crap, sorry about that."')
		print("It tries to put your hand back on, but you collapse.")
		print("The last thing you see is the bear shrug and eat you.")
		return 'death'

	elif give_it == "say no":
		print("The bear looks shocked. Nobody ever told a bear ")
		print("with a broadsword 'no'. It asks, ")
		print('"Is it because it\'s not a katana? I could go get one!"')
		print("It then runs off and now you notice a big iron gate.")
		print('"Where the hell did that cvome from?" You say.')

		return 'big_iron_gate'

	else :
		print("The bear looks puzzled as to why you'd do that.")
		return "bear_with_sword"

def big_iron_gate() :
	print("You walk up to the big iron gate and see there's a handle.")

	open_it = input(prompt)

	if open_it == 'open it':
		print("You walk along a dark passage while weird moaning sounds can be heard from afar")
		print("There's two doors at the end of the passage")
		print("Which one do you enter")
		which_door = input(prompt)

		if which_door == "door 1":
			print("You open it and you are free!")
			print("There are mountains. And berries! And...")
			print("Oh! but then the bear comes with his katana and stabs you.")
			print('"Who\'s laughing now ! ? Love this katana."')

			return 'death'

		elif which_door == "door 2":
			print("You open it and you are free!")
			print("There is stream running downhill.")
			print("You can see the bear at a distance carrying a large katana and ...")
			print('Oh ! Oh ! the bear slips and impales itself with his sword')
			print("you win")
			print("Please wait for the next part if you like the game :)")
	else :
		print("That doesn't seem sensible. I mean, the door's right there.")
		return 'big_iron_gate'

ROOMS = {
	'death' : death,
	'princess_lives_here' : princess_lives_here,
	'gold_koi_pond' : gold_koi_pond,
	'big_iron_gate' : big_iron_gate,
	'bear_with_sword' : bear_with_sword
	
}

def runner(map, start) :
	next = start

	while True :
		room = map[next]
		print("\n--------------")
		next = room()
runner(ROOMS, 'princess_lives_here')
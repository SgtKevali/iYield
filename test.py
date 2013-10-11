import sys
import random
print "Karma and Gold \n Copyright Alex Rankine 2013 - 3000 \n All Rights Reserved."

def endgame():
	print "\n Final amount of karma: " + str(stats['karma'])
	print "\n Final amount of gold: " + str(stats['gold'])
	deathQuotes = {'1': "'Our dead are never dead to us, until we have forgotten them.' -- George Eliot ", '2': "'Die, v.: To stop sinning suddenly.' -- Elbert Hubbard ", '3': "'I didn't attend the funeral, but I sent a nice letter saying I approved of it.' -- Mark Twain ", '4': "'Do not fear death so much but rather the inadequate life.' -- Bertolt Brecht ", '5': "'No one wants to die. Even people who want to go to heaven don't want to die to get there. And yet death is the destination we all share. No one has ever escaped it. And that is as it should be, because Death is very likely the single best invention of Life. It is Life's change agent. It clears out the old to make way for the new.' -- Steve Jobs ", '6': "'Everything that gets born dies.' -- Morrie Schwartz ", '7': "'Life is hard. Then you die. Then they throw dirt in your face. Then the worms eat you. Be grateful it happens in that order.' -- David Gerrold ", '8': "'Don't go around saying the world owes you a living. The world owes you nothing. It was here first.' -- Mark Twain ", '9': "'In the end, it's not the years in your life that count. It's the life in your years.' -- Abraham Lincoln ". '10': "'Death may be the greatest of all human blessings.' -- Socrates ", '11': "'We have no reliable guarantee that the afterlife will be any less exasperating than this one, have we?' -- Noel Coward ", '12': "'I don't have too much faith in destiny, or an afterlife. This is it.' -- Robin Gibb "}
	randomNumber = str(random.randint(1,12))
	print '/n' + deathQuotes[randomNumber]
	raw_input()
	sys.exit()

	
def continuegame():
	print "\n Current amount of karma: " + str(stats['karma'])
	print "\n Current amount of gold: " + str(stats['gold'])
	raw_input()

stats = {'gold': 10, 'karma': 0}

undefinedChoice = "\n Zeus himself comes down from the sky and says, 'ARE YOU TRYING TO TRICK THE GAME, PEASANT?! FEEL MY WRATH!' You die. \n \n Game over. "
victory1 = False
streetChoice = raw_input("\n You were simply walking down the street in downtown Harlem until a man, armed with a knife, confronts you. 'Give me all of your gold or feel the chill of my blade,' he whispered coldly. Do you give 'all' of your gold, 'some' of it, do you 'refuse', or do you try to 'punch' him? ")
if streetChoice == 'all':
	stats['karma'] += 2
	stats['gold'] -= stats['gold']
	raw_input("\n 'Smart choice, peon. Mwuhahahahahahahaha! See you later!' said the thug' Well, at least you're still alive. Victory achieved! Karma gained! ")
	victory1 = True

elif streetChoice == 'some':
	streetChoice2 = raw_input("\n 'DO YOU TAKE ME FOR A FOOL! GIVE ME ALL OF YOUR GOLD RIGHT NOW OR FEEL THE WRATH OF GOD!' Do you give 'all' of your gold or do you 'refuse'?' ")
	if streetChoice2 == 'all':
		stats['karma'] += 1
		stats['gold'] -= stats['gold']
		print "'Finally, I now have what I want. Goodbye.', said the thug victoriously. On the bright side, you survived the encounter. Victory achieved! Money lost... Karma gained!"
		victory1 = True

	elif streetChoice2 == 'refuse':
		stats['karma'] += 5
		raw_input("'Damn, I thought I had you there. This knife is no knife. It is simply a baby rattler,' said the man. You lean in to see if the knife is actually a baby rattler, and thankfully, it is. \n \n You defeated! Karma gained! ")
		victory1 = True
	else:
		raw_input(undefinedChoice)

elif streetChoice == 'refuse':
	stats['karma'] += 10
	raw_input("\n Oh, why must the gods be so cruel? This knife is no knife. It is simply a baby rattler,' said the man. You lean in to see if the knife is actually a baby rattler, and thankfully, it is. \n \n You defeated! Karma gained! ")
	victory1 = True

elif streetChoice == 'punch':
	stats['karma'] -= 10
	streetChoice2 = raw_input("\n Karma lost. \n You try to punch the man but he quickly ducks under it and attempts to uppercut you. Do you 'evade' or 'counter'? ")
	if streetChoice2 == 'evade':
		stats['gold'] -= stats['gold']
		print "\n While your face dodged the uppercut, unfortunately, your manhood did not. You fall onto the cold sidewalk, clutching your crotch. The man walks over and beats you to death with his bare fists. He then steals all of your gold. \n \n Money lost... Game over. "
	elif streetChoice2 == 'counter':
		stats['karma'] -= 50
		stats['gold'] += 100
		print "\n You knock away the incoming uppercut, leaving the man vulnerable. You punch and kick him until he is nothing more than a corpse on the sidewalk. You take all of his gold and feel victorious and guilty for a moment, until the police arrive and send you off to jail for fifty years with no opportunity to bail yourself out. \n \n Money gained! Karma lost... Game over. "
	else:
		raw_input(undefinedChoice)

else:
	raw_input(undefinedChoice)

if victory1 == False:
	endgame()

continuegame()

victory2 = False
print "\n \n Feeling good about yourself after properly dealing with the street thug, you finally arrive at work; a dull, boring office. \n You go to your desk, sit down, and begin to work. Several hours later, you snooze on your desk while only half of the work day is over. Eric, the office bully, comes up to you and pours steaming hot coffee on your head. 'Haha, that ought to wake you up!', he said."
officeChoice = raw_input("\n \n Feeling enraged, you decide to... 'beat' him up, 'resume' your work, or 'complain' to your manager. ")

if officeChoice == 'beat':
	stats['karma'] -= 10
	officeChoice2 = raw_input("\n \n You lose karma. \n You quickly stand up and try to roundhouse kick Eric, but he grabs your leg mid-flight and flips you over. He manically laughs as he prepares to body-slam you. On the floor, you see a knife within your reach. \n Do you use the 'knife' to defend yourself or do you try to 'roll' out of the way of Eric's body-slam? ")
	if officeChoice2 == 'knife':
		stats['karma'] -= 50
		stats['gold'] += 50
		print "\n You pick up the knife and stick it up as Eric tries to body-slam you. Eric falls down onto the knife and is stabbed in the heart. Before he dies, Eric says, 'Why did you have to pull out the knife? Why! I'm too young to die!' \n With a final sigh, Eric dies. Luckily, you are able to loot and hide his body as well as the knife in a dumpster without any in the office noticing, but you feel extremely guilty. \n \n Victory achieved! Money gained! Karma lost... "
		victory2 = True
	elif officeChoice2 == 'roll':
		stats['karma'] += 20
		print "\n You successfully roll away from Eric's body-slam, leaving Eric quite vulnerable. However, instead of continuing the conflict, you negotiate with Eric to come to a peace agreement and go off about your business. Before Eric leaves, he says 'Do not try to mess with me again or else you'll regret it!' \n \n Victory achieved! Karma gained!"
		victory2 = True
	else:
		raw_input(undefinedChoice)
elif officeChoice == 'resume':
	print "\n Although you feel as if you should beat Eric's head in or at least complain to the manager, you decide to play it cool and continuing working. 'You punking out? Well, that's right! Know your place, peasant.', snarled Eric and then left. \n \n Victory achieved! "
	victory2 = True

elif officeChoice == 'complain':
	stats['karma'] += 30
	stats['gold'] += 40
	print "\n Furious, you rise from your desk, fire through the hallway and barge into your manager's office, in which you tell the surprised manager about Eric's misbehaviour. The manager then goes to Eric and asks him to come to his office. \n They go there and minutes later, Eric kicks down the door to the manager's office and yells, 'I'm done with this damn place. This is ridiculous! I try to have some fun, but someone has to ruin it, do they?'. \n Eric glares at you for a moment and quietly says, 'You shall pay for this; You shall pay!' He then barges out of the office. The manager then informs you that you have received a raise for standing up to the office bully! \n \n Victory achieved! Money gained! Karma gained! "
	victory2 = True

else:
	raw_input(undefinedChoice)

if victory2 == False:
	endgame()

continuegame()

print "\n After a hard day of work, you go home, lie down on your comfy couch, and turn on the TV. You change the channel to Fox News, your favorite news channel, and see a frantic news-anchor reporting about, according to the headline, about a serial killer who has taken the lives of twenty people so far by shanking them and has left no trace. \n \n Suddenly, you hear a noise in the kitchen and out of it comes the serial killer himself equipped with a butcher knife. 'I have come to take your soul, human! Prepare to be vanquished!' he proclaimed. "
homeChoice = raw_input("\n You remember about your great-great-great-grandfather's katana mounted on the wall behind you. Do you use the 'katana', 'pray' to all deities of the world to bring their wrath upon the serial killer, or do you 'run' away? ")
victory3 = False

if homeChoice == 'katana':
	homeChoice1 = raw_input("You sheathe the family katana from its mount on the wall behind you and channel the force of your ancestor's blood within you. The serial killer charges at you and prepares to stab you. You ... 'parry' the stab, 'dodge' the stab, or 'stab' the serial killer first. ")
	if homeChoice1 == 'parry':
		stats['karma'] += 20
		print "\n You are unable to parry the serial killer's stab and fall to the floor. You, however, still manage to fatally wound the serial killer with a final slash across his neck. Both of you die, making the battle a tie. Karma gained! Game over. "
	elif homeChoice1 == 'dodge':
		stats['karma'] += 50
		stats['gold'] += 100
		print "\n You successfully dodge the serial killer's stab by sidestepping his attack. Not expecting this and putting all his strength into the stab, the serial killer falls to the ground. You dash over to him and stab him in chest. 'What... how did you manage to defeat me? Curses! Master Kunai, I have failed you... I make one final request, however. Destroy this man and you shall honor my death.' whispered the serial killer. As the serial killer makes a final sigh, you hear thunder crackle in the distance. You feel as if you have made a grave mistake, but figuring that you have already been indicted by the serial killer, you loot his corpse, on which you find a sum of money. Money gained! Karma gained! You defeated! " 
		victory3 = True
	elif homeChoice1 == 'stab':
		stats['karma'] += 50
		print "\n You hold out your katana straight and wait for the serial killer to blindly run into the blade. However, instead the serial killer sidesteps the katana's blade and tries to slash you with his butcher knife, but you squeeze the handle of the katana and the blade of it ejects from the handle with a rocket attached to the end of it. \n It turns and spears the serial killer to the wall. Then, it unleashes a force of energy and obliterates the serial killer, but the blade itself remains undamaged and returns itself to the hilt of the katana. You are speechless but hear a sudden crackle of thunder in the distance. Karma gained! You defeated! "
		victory3 = True
	else:
		raw_input(undefinedChoice)

elif homeChoice == 'pray':
	stats['karma'] += 100
	print "\n Almost instantly after completing your prayer and out of a sudden flash of light, Zeus himself appears in the room and uses his holy powers to shoot lightning from his fingertips and electrocute the serial killer until he is crisp as toast. You fall to your knees and praise Zeus, who gladly accepts the praise and then quickly vanishes into the unknown realm of gods. All is not well, for you hear a peculiar strike of thunder in the distance and a feeling of dread overcomes you. Karma gained! You defeated! "
	victory3 = True

elif homeChoice == 'run':
	stats['karma'] += 10
	homeChoice1 = raw_input("\n You quickly dash out of your house's door and across the street. The serial killer pursues you, but fortunately, a garbage truck that was picking garbage in your neighbourhood hits him. The serial killer cries out in pain as the garbage truck runs over him. The driver, confused, stops the garbage truck while the serial killer is restrain by one of the wheels. You decide to... 'beat' the serial killer to death or 'call' the authorities to arrest the serial killer.")
	if homeChoice1 == 'beat':
		stats['karma'] += 5
		print "\n While the serial killer struggles underneath one of the tires of the garbage truck, you punch and kick him until he lays motionless. The alarmed garbage-man sees this and tries to call the authorities, but you quickly stop and inform him that the man you just killed was the notorious serial killer. Nonetheless, the garbage-man continues to call the authorities, and soon the local police arrive and tell you to lay down all of your weapons. You try to approach one of the police officers and explain the situation to them, but they quickly become alarmed and fire upon you. Bullets hit you one by one, and soon you crumple down on the street and die from gunshot wounds. Karma gained! Game over... "
	elif homeChoice1 == 'call':
		stats['karma'] += 60
		print "\n You dial 911 and inform the local police about location of the serial killer and his state of restraint. Almost immediately, police arrive on the scene and arrest the serial killer. As he is put in handcuffs, the serial killer says to you, 'You have made a grave mistake, my friend. Mwuahahahahaha!' A policeman silences him and tells you that you are now safe. Unfortunately, a crack of thunder some miles away makes you feel as if you indeed have made a grave mistake. Karma gained! Victory achieved! "
		victory3 = True
	else:
		raw_input(undefinedChoice)

else:
	raw_input(undefinedChoice)

if victory3 == False:
	endgame()

continuegame()
raw_input("Thanks for playing. Try choosing different choices next time to see their outcome. Stay tuned for the next chapter in Karma and Gold!")
sys.exit()

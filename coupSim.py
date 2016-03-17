# initialize variables
turn = 1
player1win = False
player2win = False
player1money = 0
player2money = 0
player1influence = None
player2influence = None

# define all role functions
def duke(player1gold, player2gold, player1influence, player2influence, turn):
	if turn%2 == 1:
		player1gold = player1gold + 3
	else:
		player2gold = player2gold + 3

	goldlist = [player1gold, player2gold]
	print "duke rocks!"
	return goldlist

def captain(player1gold, player2gold, player1influence, player2influence, turn):
	if turn%2 == 1:
		if player2influence == "captain" or "ambassador":
			print "p2 is a %s" % player2influence
			player1gold = player1gold + 2
			print "countered!"	
		else:
			if player2gold == 1:
				player1gold = player1gold + 1
				player2gold = player2gold - 1

			# elif player2gold == 0 and player2influence == "duke":
			# 	player1gold = player1gold + 1

			# elif player2gold == 0:
			# 	player1gold = player1gold + 2

			else:
				player1gold = player1gold + 2
				player2gold = player2gold - 2

	else:
		if player1influence == "captain" or "ambassador":
			player2gold = player2gold + 2
			print "p1 is a %s" % player1influence
			print "countered!"
		else:
			if player1gold == 1:
				player2gold = player2gold + 1
				player1gold = player1gold - 1

			# elif player1gold == 0 and player1influence == "duke":
			# 	player2gold = player2gold + 1

			# elif player1gold == 0:
			# 	player2gold = player2gold + 2
			else:
				player2gold = player2gold + 2
				player1gold = player1gold - 2
				print "stolen!"

	print "captain rocks!"
	goldlist = [player1gold, player2gold]
	return goldlist

def contessa(player1gold, player2gold, player1influence, player2influence, turn):
	if turn%2 == 1:
		if player2influence == "duke":
			player1gold = player1gold + 1
		else:
			player1gold = player1gold + 2


	else:
		if player1influence == "duke":
			player2gold = player2gold + 1
		else:
			player2gold = player2gold + 2


	goldlist = [player1gold, player2gold]
	return goldlist

def assassin(player1gold, player2gold, player1influence, player2influence, turn):
	if turn%2 == 1:
		if player2influence == "duke":
			player1gold = player1gold + 1
		else:
			player1gold = player1gold + 2

	
	else:
		if player1influence == "duke":
			player2gold = player2gold + 1
		else:
			player2gold = player2gold + 2

	goldlist = [player1gold, player2gold]
	return goldlist

influences = {"duke":duke,"captain":captain,"contessa":contessa,"assassin":assassin}

# Ask inputs
print "what is Player 1's influence?"
player1influence = raw_input().lower()

print "what is Player 2's influence?"
player2influence = raw_input().lower()


# Run the sim for every possible money combination 

# iterate all player 1 money
for i in range(0,7):

	# iterate all player 2 money
	for j in range(0,7):

		playermoney = [i,j]
		print "\n--------------evaluating p1 %d and p2 %d-------------------" %(i, j)

		#run through turns as long as the no one has won
		while (player1win == False and player2win == False):
			# run player1 role if odd turn
			if turn%2 == 1:
				if playermoney[0] >= 3 and player1influence == "assassin" and player2influence != "contessa":
					player1win = True
					if player1influence == "assassin":
						playermoney[0] = playermoney[0] - 3
					else:
						playermoney[0] = playermoney[0] - 7
					break

				elif playermoney[0] >= 7:
					player1win = True
					if player1influence == "assassin":
						playermoney[0] = playermoney[0] - 3
					else:
						playermoney[0] = playermoney[0] - 7
					break

				else:
					playermoney = influences[player1influence](playermoney[0], playermoney[1], player1influence, player2influence, turn)
				print "turn %d: p1 gold is %d       p2 gold is %d" %(turn, playermoney[0], playermoney[1])

			# run player2 role if even turn
			else:
				if playermoney[1] >= 3 and player2influence == "assassin" and player1influence != "contessa":
					player2win = True
					if player1influence == "assassin":
						playermoney[1] = playermoney[1] - 3
					else:
						playermoney[1] = playermoney[1] - 7
					break

				elif playermoney[1] >= 7:		
					player2win = True
					if player2influence == "assassin":
						playermoney[1] = playermoney[1] - 3
					else:
						playermoney[1] = playermoney[1] - 7
					break

				else:
					playermoney = influences[player2influence](playermoney[0], playermoney[1], player1influence, player2influence, turn)
				print "turn %d: p2 gold is %d       p1 gold is %d" %(turn, playermoney[1], playermoney[0])
			
			turn += 1

		if player1win == True:
			print "At %d, %d, player 1 wins. Player 1 has %d gold. Player 2 has %d gold." %(i,j,playermoney[0], playermoney[1])
		elif player2win == True:
			print "At %d, %d, player 2 wins. Player 1 has %d gold. Player 2 has %d gold." %(i,j,playermoney[0], playermoney[1])
		else:
			print "something is very wrong"
		player1win = False
		player2win = False
		turn = 1



	print "finished testing one value of i j"

print "finished testing one value of all values of j for 1 i"



	
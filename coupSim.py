# initialize variables
import json
import csv


indTest = "no"
turn = 1
player1win = False
player2win = False
player1money = 0
player2money = 0
player1influence = None
player2influence = None
dukeoutcome={}
captainoutcome={}
contessaoutcome={}
assassinoutcome={}

outcomedict ={"duke":dukeoutcome,"captain":captainoutcome,"contessa":contessaoutcome,"assassin":assassinoutcome}
rolelist =["duke","captain","contessa","assassin"]

# define all role functions
def duke(player1gold, player2gold, player1influence, player2influence, turn):
	if turn%2 == 1:
		player1gold = player1gold + 3
	else:
		player2gold = player2gold + 3

	goldlist = [player1gold, player2gold]
	return goldlist

def captain(player1gold, player2gold, player1influence, player2influence, turn):
	if turn%2 == 1:
		if player2influence == "captain":
			player1gold = player1gold + 2
			print "countered!"	
		else:
			if player2gold == 1:
				player1gold = player1gold + 1
				player2gold = player2gold - 1

			elif player2gold == 0 and player2influence == "duke":
				player1gold = player1gold + 1

			elif player2gold == 0:
				player1gold = player1gold + 2

			else:
				player1gold = player1gold + 2
				player2gold = player2gold - 2

	else:
		if player1influence == "captain":
			player2gold = player2gold + 2
			print "countered!"
		else:
			if player1gold == 1:
				player2gold = player2gold + 1
				player1gold = player1gold - 1

			elif player1gold == 0 and player1influence == "duke":
				player2gold = player2gold + 1

			elif player1gold == 0:
				player2gold = player2gold + 2
			else:
				player2gold = player2gold + 2
				player1gold = player1gold - 2
				print "stolen!"

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

# Do you want to run individual test?
print "Do you want to run test for specific role combinations?"
indTest = raw_input().lower()

if indTest == "yes":
	# Ask inputs
	print "what is Player 1's influence?"
	player1influence = raw_input().lower()

	print "what is Player 2's influence?"
	player2influence = raw_input().lower()


	# Run the sim for every possible money combination for 2 given roles

	# iterate all player 1 money
	for i in range(0,7):

		# iterate all player 2 money
		for j in range(0,7):

			playermoney = [i,j]
			print "\n--------------evaluating p1 %d and p2 %d-------------------" %(i, j)
			print "p1 is %s, p2 is a %s" % (player1influence, player2influence)

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
				#store outcome in dictionary
				outcomedict[player1influence][str(player2influence)+str(i)+str(j)] = "win"

			elif player2win == True:
				print "At %d, %d, player 1 loses. Player 1 has %d gold. Player 2 has %d gold." %(i,j,playermoney[0], playermoney[1])
				#store outcome in dictionary
				outcomedict[player1influence][str(player2influence)+str(i)+str(j)] = "lose"

			else:
				print "something is very wrong"
			player1win = False
			player2win = False
			turn = 1



		print "=========finished testing all values of j for %d \n\n" %i

	print "for a %s : %s" %(player1influence, outcomedict[player1influence].items())

else:
	print "OK! Going through every possibility!"
	#iterate through all possible roles for p1
	for role1 in rolelist:
		player1influence = role1

		#iterate through all possible roles for p2
		for role2 in rolelist:
			player2influence = role2

			# Run the sim for every possible money combination for 2 given roles

			# iterate all player 1 money
			for i in range(0,7):

				# iterate all player 2 money
				for j in range(0,7):

					playermoney = [i,j]
					print "\n--------------evaluating p1 %d and p2 %d-------------------" %(i, j)
					print "p1 is %s, p2 is a %s" % (player1influence, player2influence)

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
						#store outcome in dictionary
						outcomedict[player1influence][str(player2influence)+str(i)+str(j)] = "win"

					elif player2win == True:
						print "At %d, %d, player 1 loses. Player 1 has %d gold. Player 2 has %d gold." %(i,j,playermoney[0], playermoney[1])
						#store outcome in dictionary
						outcomedict[player1influence][str(player2influence)+str(i)+str(j)] = "lose"

					else:
						print "something is very wrong"
					player1win = False
					player2win = False
					turn = 1

	print"wow that was tough!"
	print "for a duke : %s \n\n" %(outcomedict["duke"].items())
	print "for a captain : %s \n\n" %(outcomedict["captain"].items())
	print "for a contessa : %s \n\n" %(outcomedict["contessa"].items())
	print "for a assassin : %s \n\n" %(outcomedict["assassin"].items())

#write
writer1 = csv.writer(open('dukeData.csv', 'wb'))
for key1, value1 in outcomedict["duke"].items():
   writer1.writerow([key1, value1])

writer2 = csv.writer(open('assassinData.csv', 'wb'))
for key2, value2 in outcomedict["assassin"].items():
   writer2.writerow([key2, value2])

writer3 = csv.writer(open('captainData.csv', 'wb'))
for key2, value2 in outcomedict["captain"].items():
   writer3.writerow([key2, value2])

writer4 = csv.writer(open('contessaData.csv', 'wb'))
for key2, value2 in outcomedict["contessa"].items():
   writer4.writerow([key2, value2])










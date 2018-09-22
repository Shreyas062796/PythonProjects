import random
import sys #decided to have command line arguement instead of standard io because
#I thought that it would definitely be faster 

#have two players and each of the have to choose rock,paper or scissors
#edge cases: if they choose the same thing then it would have neither
#and need to keep running until they are different or you can just count it as neither

#could have implemented in such a way that it would keep going until there was a winner
#but I thought that its better to know how many times that neither of them won as well
def RockPaperScissors():
	choices = {0:"scissors",1:"paper",2:"rock"}
	#chooses two random choices
	p1choice = random.choice(list(choices))
	p2choice = random.choice(list(choices))

	# print(p1choice)
	# print(p2choice)

	# scissors beats paper, paper beats rock, rock beats scissors
	#could have definitely found a more efficient way of doing this
	if(p1choice == p2choice):
		return("neither")
	elif(p1choice == 2 and p2choice == 0):
		return(["p1",choices[p1choice]])
	elif(p1choice == 0 and p2choice == 2):
		return(["p2",choices[p2choice]])
	elif(p1choice < p2choice):
		return(["p1",choices[p1choice]])
	else:
		return(["p2",choices[p2choice]])

#runs the game a number of times based on the command line arguement and then
#would return the number of times each player won and the number of times that
#rock,paper and scissors won
def playGame(times):
	winners = {"player1wins":0,"player2wins":0,"neither": 0}
	winningChoice = {"rock":0,"scissors":0,"paper":0,"neither": 0}
	for i in range(times):
		game = RockPaperScissors()
		if(game[0] == "p1"):
			winners["player1wins"] += 1
			winningChoice[game[1]] += 1
		elif(game[0] == "p2"):
			winners["player2wins"] += 1
			winningChoice[game[1]] += 1
		else:
			winners["neither"] += 1
			winningChoice["neither"] += 1

	# print(winners)
	# print(winningChoice)
	return(winners,winningChoice)
if __name__== "__main__":
	print(playGame(int(sys.argv[1])))
	
# WumpusChallenge.py

from random import randrange
import sys

# Create grid of room - 4 X 5 grid with sequentially numbered rooms

class Wumpus:

	def __init__(self, n_rows, n_cols):
		self.make_maze(n_rows, n_cols)

	def make_maze(self, n_rows, n_cols):
		maze = {0:(1,4,5), 1:(0,2,5), 2:(1,3,6), 3:(2,6,7), 4:(0,5,8), 5:(1,4,5),\
		 6:(2,3,7), 7:(3,6,11), 8:(4,9,12), 9:(8,10,12), 10:(9,11,12), 11:(7,10,15), \
		 12:(9,13,16), 13:(12,16,17), 14:(15,18,19), 15:(11,14,19), 16:(12,13,17), \
		 17:(13,16,18), 18:(14,17,19), 19:(14,15,18)}
		self.choose(maze)

	def choose(self, maze):
		rooms = len(maze)
		Wumpus_location = randrange(rooms)
		pit_location = randrange(rooms)
		if pit_location == Wumpus_location:
			pit_location = randrange(rooms)
		bat_location = randrange(rooms)
		if bat_location == Wumpus_location or pit_location:
			bat_location = randrange(rooms)
		player_location = randrange(rooms)
		if player_location == Wumpus_location or pit_location or bat_location:
			player_location = randrange(rooms)
		self.move(maze, player_location, Wumpus_location, pit_location, bat_location)

	def move(self, maze, player_location, Wumpus_location, pit_location, bat_location):
		self.pit_location = pit_location
		self.bat_location = bat_location
		new_move = int(input("Into which room would you like to move? " + str(maze[player_location]) + " "))
		player_location = new_move
		if player_location == Wumpus_location:
			print("Oh, no! The Wumpus! Aaaaarrrrgh!")
			sys.exit()
		elif player_location == pit_location:
			self.pit()
		elif player_location == bat_location:
			self.bats(maze, player_location, Wumpus_location, pit_location, bat_location)
		else:
			for item in maze[player_location]:
				if Wumpus_location == item:
					print("I smell a Wumpus\n")
					self.shoot(maze, player_location, Wumpus_location, pit_location, bat_location)
			else: 
				self.move(maze, player_location, Wumpus_location, pit_location, bat_location)

	def shoot(self, maze, player_location, Wumpus_location, pit_location, bat_location):
		decision = input("Which do you want to do, move or shoot? ")
		if decision == "move":
			self.move(maze, player_location, Wumpus_location, pit_location, bat_location)
		else:
			fire = int(input("Into which room would you like to shoot? " + str(maze[player_location]) + " "))
			if fire == Wumpus_location:
				print("Congratulations! You killed the Wumpus!")
				sys.exit()
			else:
				print("Oh, no! The Rumpus wasn't there! It's coming to kill you")
				sys.exit()

	def pit(self):
		print("You've fallen into the bottomless pit! Aaaaarrrrgh!")
		sys.exit()

	def bats(self, maze, player_location, Wumpus_location, pit_location, bat_location):
		self.maze = maze
		print("Rats, it's bats! They have chased you to another location!")
		player_location = randrange(20)
		if player_location == Wumpus_location or pit_location or bat_location:
			player_location = randrange(20)
		self.move(maze, player_location, Wumpus_location, pit_location, bat_location)

print("Welcome to the game of Wumpus. To win, you must make your way\n, \
into a room next to the Wumpus and kill him by shooting your one arrow\n \
into the room he is in. If you choose wrong, the Wumpus kills you.\n, \
If you walk into the room with the Wumpus, the Wumpus will kill you.\n,  \
Oh, and did I mention that one room conatins bats that will chase you\n \
to another and another room has a bottomless pit in it. If you fall\n \
into it, you die. Have fun!")

num_rows = 5
num_cols = 4
Wumpus(num_rows, num_cols)
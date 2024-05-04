from getpass import getpass as input

intro = ("--------E P I C  🪨  📃 ✂️   B A T T L E-------- ")
print(intro.center(100))

print("\nselect you move Rock, Paper or Scissor (pleas enter R, P or S)\n")

player_1 = input("enter your move player 1 ---> ")
player_2 = input("\nenter your move player 2 ---> ")

if (player_1 == "R" or player_1 == "r") and (player_2 == "R"
                                             or player_2 == "r"):
  print("\033[31m", "\nit's an tie!!!!!😮😮 both picked rock", "\033[0m")
elif (player_1 == "R" or player_1 == "r") and (player_2 == "P"
                                               or player_2 == "p"):
  print("\033[32m", "\nplayer 2 won as paper smash the rock!!!!!🥳🥳", "\033[0m")
elif (player_1 == "R" or player_1 == "r") and (player_2 == "S"
                                               or player_2 == "s"):
  print("\033[33m", "\nplayer 1 won as rock smash scisoor!!!!!🥳🥳", "\033[0m")

elif (player_1 == "P" or player_1 == "p") and (player_2 == "R"
                                               or player_2 == "r"):
  print("\033[33m", "\n PLAYER 1 won paper smash roch!!!!!🥳🥳", "\033[0m")
elif (player_1 == "P" or player_1 == "p") and (player_2 == "P"
                                               or player_2 == "p"):
  print("\033[31m", "\nit's an tie!!!!!😮😮 both pick paper", "\033[0m")
elif (player_1 == "P" or player_1 == "p") and (player_2 == "S"
                                               or player_2 == "s"):
  print("\033[32m", "\n PLAYER 2 won as scissor smash paper!!!!!🥳🥳", "\033[0m")

elif (player_1 == "S" or player_1 == "s") and (player_2 == "R"
                                               or player_2 == "r"):
  print("\033[32m", "\nplayer 2 won as rock smash scissor!!!!!🥳🥳", "\033[0m")
elif (player_1 == "S" or player_1 == "s") and (player_2 == "P"
                                               or player_2 == "p"):
  print("\033[33m", "\nplayer 1 won as scissor smash paper!!!!!🥳🥳", "\033[0m")
elif (player_1 == "S" or player_1 == "s") and (player_2 == "S"
                                               or player_2 == "s"):
  print("\033[31m", "\nit's an tie!!!!!😮😮 both picked scissor", "\033[0m")
else:
  print("\033[31m", "\n\nERROR")
  print(
      "WRONG INPUT, make sure both players put (R, P or S or it's corresponding lowercase ONLY)",
      "\033[0m")

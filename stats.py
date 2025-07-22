import argparse
import pdb

parser = argparse.ArgumentParser(description="Python Sports Statistics")
parser.add_argument('--debug', help='use pdb to look into code before exiting program', action='store_true')

# Here are two examples of "global" variables. We typically define them at the top of the program so that they are
# easy to edit. Use ALL CAPS to distinguish globals from normal variables we define inside the main function.
# TODO: Edit these as needed or add other globals here if you find it helpful.
SPORT = "Basketball"
FILENAME = "basketball_team2324.txt"
INFILE = open(FILENAME, 'r')

# statistics questions to include: best scoring efficiency, Best Defensive player, projected starting 5, most versatile player

def main(args):
	while True:
		# describes the program to the user, provides a list of the 23-24 basketball roster
		print("\n=========================================================================================")
		print("This is a stat searcher for the Florida Southern College Basketball team (2023 - 2024 season)")
		print("=========================================================================================\n")
		print()
		print("This is the roster for the 2023 - 2024 season")
		print("=========================================================================================")

		print("Akol Arop\nDominick Denny\nJadin Booth\nErickson Bans\nJoe Moon\nDonovan Smith\nWes Bongiorni\nNoah Louis\nRiley Buccino\nLuke Reilly\nConnor Raines\nConor O'Connell\nAlex Steen\nSam Walters\nTrey Jones\nLuke Anderson")

		print("=========================================================================================\n")

		# prompts the user for input to use in stat finder function
		name = input("Please enter the player you would like to stat search for: ")
		print()
		stat = input("Please enter one these stats to search for (Number/Position/Height/Weight/Total points/Total rebounds/Games played/Assists/Steals/Blocks/FG%): ")
		print()
		print("=========================================================================================")

		# calling the function
		stat_finder(name, stat)

		print("=========================================================================================")
		print()

		# while loop to ask if the user wants to see another stat for the same player
		STATANSWER = input("Would you like to choose another stat for the same player? ")
		while STATANSWER.capitalize() == "Yes":
			print()
			stat = input("Please enter one these stats to search for (Number/Position/Height/Weight/Total points/Total rebounds/Games played/Assists/Steals/Blocks/FG%): ")
			print("\n=========================================================================================")
			stat_finder(name, stat)
			print("=========================================================================================\n")
			STATANSWER = input("Would you like to choose another stat for the same player? ")


		# asks player if they would like to choose a different player, restarts the loop if they say yes
		print()
		playeranswer = input("Would you like to choose a different player? ")
		if playeranswer.capitalize() == "Yes":
			continue
		print()

		# asks user if they want to exit the program, then breaks the indefinite loop if they say yes
		print()
		exitanswer = input("Would you like to exit the program? ")
		if exitanswer.capitalize() == "Yes":
			break
		print()

	# The if-statement below allows you to (optionally) debug your program
	# To trigger this code, run "python stats.py --debug" at the command line
	if args.debug:
		pdb.set_trace()
	
# this function takes the name entered by the user, goes through each line to match the name, then creates a dictionary of that line when matched,
# where the stat chosen by the user can then be used as a key word for the dictionary
def stat_finder(name, stat):
	f = open(FILENAME, 'r')
	for line in f:
		lsplit = line.split("//")
		ldex = lsplit[1]
		lname = ldex[6:]
		if lname == name:
			statdict = {'Number':lsplit[0], 'Position':lsplit[2], 'Height':lsplit[3], 'Weight':lsplit[4], 
			'Total points':lsplit[5], 'Total rebounds':lsplit[6], 'Games played':lsplit[7], 'Assists':lsplit[8], 
			'Steals':lsplit[9], 'Blocks':lsplit[10], 'FG%':lsplit[11]}
			print(statdict[stat])
	f.close()


if __name__ == "__main__":
	main(parser.parse_args())

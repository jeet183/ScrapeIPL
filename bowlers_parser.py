import csv

player_name = input("Enter player's actual name\n")
opposition_team = input("Enter opposition's abbreviated name\n")
ground = input("Enter ground name\n")
print()
print("Player Name: " +player_name)
print("Opposition Team: " +opposition_team )
print("Ground: " +ground)
with open('bowlers_real.csv','r') as csv_file:
	csv_reader = csv.reader(csv_file)
	for line in csv_reader:
		if( player_name in line[0] ):
			if(opposition_team in line[6]):
				if(ground in line[7]):
						print(line)

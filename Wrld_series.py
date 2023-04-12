def main():
    team = input("Enter the name of a team: ")
    if team.lower() == 'quit':
        return None
    else:
        winners = read_file('WorldSeriesWinners.txt')
        search_team(team, winners)

#Reads the file and puts it into list
def read_file(filename):
    with open(filename, 'r') as file:
        winners = []
        for line in file:
            winners.append(line.strip())
    return winners

#If the given name is in the list, every instance is counted and added
#To get the total number of wins.
def search_team(team, winners):
    wins = 0
    for winner in winners:
        if winner.lower() == team.lower():
            wins += 1
    print(f"The {team} won the world series {wins} times between 1903 and 2009.")
    main()


if __name__ == '__main__':
    main()

import random
reward = 0
user = 0
opendoor = 0
games = 1000
doorswap = False
def rungame(doorswap):
    wins = 0
    swaps = 0
    if doorswap == True:
        print("Running game by always swapping doors...")
    else:
        print("Staying on players first choice...")
    for i in range(games):
        user = random.randint(1,3)
        reward = random.randint(1,3)
        swapped = ""
        while True:
            opendoor = random.randint(1,3)
            if opendoor != user and opendoor != reward:
                break
        if doorswap == True:
            for x in range(1,4):
                if x != user and x != opendoor:
                    swapped = "Swapped from " + str(user) + " to " + str(x)
                    user = x
                    swaps += 1
                    break
        if user == reward:
            wins += 1
    print(f"Win percentage: {100*wins/games}%")
print(f"Monty hall - {games} games:")
rungame(True)
rungame(False)

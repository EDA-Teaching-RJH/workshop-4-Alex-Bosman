

# 50 20 10 5
def coffeeMachine():
    print("aaaa")
    change = 0
    while change <= 75:
        userInput = str(input("Insert a coin: "))
        match userInput:
            case "50":
                change += 50
            case "20":
                change += 20
            case "10":
                change += 10
            case "5":
                change += 5
            case _:
                print("Input not recognised.")
    print(f"change owed: {change-75}p")



''' implement a program that prompts the user to insert a coin, one at a time, each
time informing the user of the amount due. Once the user has inputted at least 75p, output how much
change they are owed. Make the assumption that the user will only enter integers, and ignore any unknown
currency denomination.'''

'''Once you have a working coffee machine, add more drinks to the system maybe hot chocolate and tea? or
even add extra options like asking the user if they want an extra shot?'''


if __name__ == "__main__":
    coffeeMachine()

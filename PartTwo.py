
def coffeeMachine():
    choiceFlag = False
    while not choiceFlag:
        choiceFlag = True
        print("Drinks: (1) flat while, (2) latte, (3) espresso, (4) tea")
        drinkChoice = int(input("Input your drink choice number: "))
        if drinkChoice == 1:
            drinkPrice = 75
        elif drinkChoice == 2:
            drinkPrice = 100
        elif drinkChoice == 3:
            drinkPrice = 50
        elif drinkChoice == 4:
            drinkPrice = 25
        else:
            print("Input not recognised")
            choiceFlag = False
    change = 0
    payFlag = False
    while not payFlag:
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
        if change >= drinkPrice:
            payFlag = True
    print(f"change owed: {change-drinkPrice}p")


if __name__ == "__main__":
    coffeeMachine()

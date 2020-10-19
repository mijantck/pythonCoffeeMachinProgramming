
#miajnur rahman
water = 400
milk = 540
coffee_beans = 120
cups = 9
money = 550
action_input = " "
buy_type = 0

def showavailblematrial():
    print("The coffee machine has:")
    print(str(water) + " of water ")
    print(str(milk) + " of milk ")
    print(str(coffee_beans) + " of coffee beans ")
    print(str(cups) + " of disposable  cups ")
    print(str(money) + " of money ")

def mainFunction() :
    print("Write action ( buy, fill, take, remaining, exit)")
    action_input = input()
    print("> " + action_input)
    function(action_input)

def function(action_input):
    global water, coffee_beans, cups, money, milk, buy_type

    if action_input == "buy":
        print("What do you want buy? 1 - espresso, 2 - latter, 3 - cappuccino")
        buy_type = int(input())
        if buy_type == 1:
            if water > 250 and coffee_beans > 16 and cups > 1:
                water -= 250
                coffee_beans -= 16
                cups -= 1
                money += 4
                print("I have enough resources, making your a coffee ")
            else:
                if water < 250:
                    print("sorry, not enough water")
                elif coffee_beans < 16:
                    print("sorry, not enough coffee been")
                elif cups < 1:
                    print("sorry, not enough Cups")

                #showavailblematrial()
        elif buy_type == 2:
            if  water > 350 and coffee_beans > 20 and milk > 75 and cups > 1:
                water -= 350
                milk -= 75
                coffee_beans -= 20
                cups -= 1
                money += 7
                print("I have enough resources, making your a coffee ")
            else:
                if water < 350:
                    print("sorry, not enough water")
                elif coffee_beans < 20:
                    print("sorry, not enough coffee been")
                elif milk < 75:
                    print("sorry, not enough milk")
                elif cups < 1:
                    print("sorry, not enough Cups")
             #showavailblematrial()
            mainFunction()
        elif buy_type == 3:
            if water > 200 and coffee_beans > 12 and milk > 100 and cups > 1:
                water -= 200
                milk -= 100
                coffee_beans -= 12
                cups -= 1
                money += 6
                print("I have enough resources, making your a coffee ")
            else:
                if water < 200:
                    print("sorry, not enough water")
                elif coffee_beans < 12 :
                    print("sorry, not enough coffee been")
                elif milk < 100:
                    print("sorry, not enough milk")
                elif cups < 1:
                    print("sorry, not enough Cups")

            # showavailblematrial()
            mainFunction()

    elif action_input == "fill":
        print("write how many ml of water do you to add :")
        water1 = int(input())
        print("> " + str(water1))
        water += water1
        print("write how many ml of milk do you to add :")
        milk1 = int(input())
        print("> " + str(milk1))
        milk = milk + milk1

        print("write how many grams of coffee beans do you to add :")
        coffee_beans1 = int(input())
        print("> " + str(coffee_beans1))
        coffee_beans += coffee_beans1

        print("write how many disposable cups  of coffee  do you to add :")
        cups1 = int(input())
        print("> " + str(cups1))
        cups += cups1
        showavailblematrial()
        mainFunction()

    elif action_input == "take":
        print("I gave you $" + str(money))
        money = 0
        showavailblematrial()
        mainFunction()

    elif action_input == "remaining":
        showavailblematrial()
        mainFunction()

mainFunction()

water = 300
milk = 65
coffee_beans = 100
cups  = 0

one_cup_make_coffee_water = 200
one_cup_make_coffee_milk = 50
one_cup_make_coffee_coffee_beans = 15

available_water = 0
available_milk = 0
available_coffee_beans = 0

availale_list = [0 , 0 , 0]

available_cups = 0
current_available_cups = 0



print("write how many ml of water the coffee machine has:")
water = int(input())
print("> " + str(water))

print("write how many ml of milk the coffee machine has:")
milk = int(input())
print("> " + str(milk))

print("write how many grams of coffee beans the coffee machine has:")
coffee_beans = int(input())
print("> " + str(coffee_beans))

available_water = int( water / one_cup_make_coffee_water)
available_milk = int(milk / one_cup_make_coffee_milk)
available_coffee_beans = int(coffee_beans / one_cup_make_coffee_coffee_beans)

current_available_cups = min(available_water,available_milk,available_coffee_beans)

print("write how many cups of coffee you will need:")
cups = int(input())
print("> " + str(cups))

available_cups = available_milk - cups


if (cups * one_cup_make_coffee_water) <= water and (cups * one_cup_make_coffee_milk) <= milk and (cups * one_cup_make_coffee_coffee_beans) <= coffee_beans :
    print("Yes, I can make that amount of coffee ")
else:
    print("No, I can ont make only "+str(current_available_cups) + " cups amount of coffee ")


#
# print('> ' + str(cups))
# print("For" + str(cups) + " cups of coffee you will need:")
# print(str(cups * water) + " ml of water")
# print(str(cups * milk) + " ml of milk")
# print(str(cups * coffee_beans) + " g of coffee beans")





print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

#pizza size code
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong input")

#pepperoni code

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 4


#extra cheese code

if extra_cheese == "Y":
    bill += 1

print(f"your final bill is ${bill}.")




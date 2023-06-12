Name:Niringiyimana Reverien
Registration Number:221012906
Department:Computer science
  
import random
num_guests = int(input("Enter the number of friends joining (including you):\n"))
if num_guests <= 0:
    print("No one is joining for the party")
else:
    guests = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(num_guests):
        name = input()
        guests[name] = 0
    total_bill = float(input("Enter the total bill value:\n"))
    split_value = round(total_bill / num_guests, 2)
    for name in guests:
        guests[name] = split_value
    print("Do you want to use the randomizer? (yes/no)")
    res = input()
    if res.lower() == "yes":
        lucky = random.choice(list(guests.keys()))
        print("{} is the lucky one!".format(lucky))      
        for i in guests:
            guests.update({lucky: 0})
            if i == lucky:
                guests.update({lucky: 0})
            else:
                split_value = round(total_bill / (num_guests - 1), 2)
                guests.update({i: round(float(split_value), 2)})
        print(guests)
    else:
        print("No one is going to be lucky")
        print(guests)

  

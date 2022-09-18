import random

def rolldice():
   dicetotal = random.randint(1,6)
   return dicetotal

def main():
    vname1 = input("Enter player 1's name:\n")
    vname2 = input("Enter player 2's name:\n")


    roll1 = rolldice()
    roll2 = rolldice()

    if roll1 == roll2:
       print("It's a tie", str(roll1))
    elif roll1 > roll2:
        print(vname1, "wins!", str(roll1), 'to', str(roll2))
    else:
        print(vname2, "wins!", str(roll2), 'to', str(roll1))

main()
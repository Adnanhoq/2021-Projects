rock = 'r'
paper = 'p'
scissors ='s'
import random

aiscore = 0
rpsscore = 0
rpsloop = 0
rpswinscore = 3
print("Rock, paper, scissors against an AI\n")
while rpsloop == 0:
    rpsnum = random.randint(1, 3)
    rps = input("rock, paper or scissors: ")
    if rps == "upleftdownright":
        print("\ncheat score activated")
        rpswinscore = int(input("change winning score: "))
    elif rps == rock:
        if rpsnum == 1:
            print("\n😐 🥌  🥌 💻\nTie")
        elif rpsnum == 2:
            print("\n😭 🥌  📄 💻\nLoser")
            aiscore = aiscore + + 1
        elif rpsnum == 3:
            print("\n😁 🥌  ✂️ 💻\nWinner")
            rpsscore = rpsscore + + 1
    elif rps == paper:
        if rpsnum == 1:
            print("\n😁 📄  🥌 💻\nWinner")
            rpsscore = rpsscore + + 1
        elif rpsnum == 2:
            print("\n😐 📄  📄 💻\nTie")
        elif rpsnum == 3:
            print("\n😭 📄  ✂️ 💻\nLoser")
            aiscore = aiscore + + 1
    elif rps == scissors:
        if rpsnum == 1:
            print("\n😭 ✂️  🥌 💻\nLoser")
            aiscore = aiscore + + 1
        elif rpsnum == 2:
            print("\n😁 ✂️  📄 💻\nWinner")
            rpsscore = rpsscore + + 1
        elif rpsnum == 3:
            print("\n😐 ✂️  ✂️ 💻\nTie")
    elif rps != "upleftdownright":
        print("\nChoice not recognised")

    if rpsscore == rpswinscore:
        rpsloop = rpsloop + + 1
    elif aiscore == rpswinscore:
        rpsloop = rpsloop + + 1

    if rpsscore == rpswinscore:
        print("\nYou've won! 😁")
        rpsloop = int(input("Enter 0 if you would like to play again, 1 to stop: "))
        aiscore = 0
        rpsscore = 0
    elif aiscore == rpswinscore:
        print("\nYou lost 😭")
        rpsloop = int(input("Enter 0 if you would like to play again, 1 to stop: "))
        aiscore = 0
        rpsscore = 0

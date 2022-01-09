import random

number =4
number = random.randint(1,9)
intro = input("guess the number between 1 and 9 :")
print(intro)
if (intro == 4):
    print("YOU WON!")
else :
    print("YOU LOST!")
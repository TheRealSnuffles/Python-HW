ROCK=1
PAPER=2
SCISSORS=3
def main():
    y=0
    x=0
    import random
    number=random.randint(1,3)
    if number==1:
        x=ROCK
    elif number==2:
        x=PAPER
    else:
        x=SCISSORS
    user=int(input("Enter 1 for rock, 2 for paper, or 3 for scissors: "))
    print(x)
    if user==number:
        print('wa wa wa try again')
    elif user==ROCK:
        y=ROCK
    elif user==PAPER:
        y=PAPER
    else:
        y=SCISSORS
    c=comp(x,y)
    print(c)
def comp(x,y):
    if y==2 and x==1:
        print("Paper covers rock, you win")
    elif y==3 and x==1:
        print("Rock smashes scissors, you lose")
    elif y==3 and x==2:
        print("Scissors cuts paper, you win")
    elif y==2 and x==3:
        print("Scissors cut paper, you lose")
    elif y==1 and x==3:
        print("Rock smashes scissors, you win")
    elif y==1 and x==2:
        print("Paper covers rock, you lose")
main()

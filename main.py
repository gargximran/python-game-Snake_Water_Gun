import random

start = 1
myPoint = 0
comPoint = 0
while start < 11:
    code = ['snake', 'water', 'gun']
    value = input("(1) snake\n(2) water\n(3) gun\nEnter your choice : ")
    if not value or not value.isnumeric():
        print("\nWrong choice! Please try with right choice.\n\n")
        continue

    if int(value) == 1:
        code.pop(int(value)-1)
        if random.randint(0, 1) == 1:

            print(f"\n\nComputer choose: {code[1]}\nYou lose\n")
            comPoint += 1
        else:
            print(f"\n\nComputer choose: {code[0]}\nYou win\n")
            myPoint += 1
        start += 1
    elif int(value) == 2:
        code.pop(int(value)-1)
        if random.randint(0, 1) == 1:
            print(f"\n\nComputer choose: {code[1]}\nYou win\n")
            myPoint += 1
        else:
            print(f"\n\nComputer choose: {code[0]}\nYou lose\n")
            comPoint += 1
        start += 1
    elif int(value) == 3:
        code.pop(int(value)-1)
        if random.randint(0, 1) == 1:
            print(f"\nComputer choose: {code[1]}\nYou lose\n")
            comPoint += 1
        else:
            print(f"\n\nComputer choose: {code[0]}\nYou win\n")
            myPoint += 1
        start += 1
    else:
        print("Wrong choice! Please try with right choice.")


if myPoint > comPoint:
    print("Congratulation you win.")
elif myPoint < comPoint:
    print("You lose! Better luck next time.")
else:
    print("Match tie")

print(f"Your Point : {myPoint}\nComputer Point : {comPoint}")
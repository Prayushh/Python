secret_number=8
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=int(input("Guess a number: "))
    if guess==secret_number:
        print("You're right")
        break
    guess_count+=1
else:
    print("Sorry you failed!")

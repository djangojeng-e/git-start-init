import random from randint 

answer = randint(0,100+1)
print(answer) 

count = 1

def compare_guess():
    while count <= 3:
        guess = int(input('Hi, guess the num(1~100)'))
        if answer == guess:
            print("You guesses correct Number bro!")
            break
        else:
            print("You messed up with guess bro! Try again mate!") 

        count = count + 1 

compare_guess()


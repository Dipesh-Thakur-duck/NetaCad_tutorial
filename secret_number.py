secret_number = 123
user_input = int(input("Guess the secret number: "))
while user_input != secret_number:
    print("Ha ha! You're stuck in my loop!")
    user_input = int(input("Guess the secret number: "))
else:
    print("Well done, muggle! You are free now.")
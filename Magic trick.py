letter = list(input())
uletters = set(letter)
guess = len(letter) == len(uletters)
if guess:
    print("1")
else:
    print("0")

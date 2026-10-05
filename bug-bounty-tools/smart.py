import random

code = random.randint(10, 10000)  # new random code each time
low, high = 10, 100
tries = 0

print(f"Target is hidden (10-100), attacking...")

while low <= high:
    guess = (low + high) // 2
    tries += 1
    print(f"Try {tries}: guessing {guess}")
    if guess == code:
        print(f"SMART CRACKED in {tries} tries! Code was {code}")
        break
    elif guess < code:
        print(" -> Too low")
        low = guess + 1
    else:
        print(" -> Too high")
        high = guess - 1

import itertools
import string
import random
import requests
import time
from colorama import Fore, Style, init
#from plyer import notification

init()
war = True


def checkUsername(username):
    global war
    url = f"https://auth.roblox.com/v1/usernames/validate?Username={username}&Birthday=2000-01-01"
    try:
        result = requests.get(url)
        responseData = result.json()
        code = responseData.get("code")
        if code == 0:
            print(Fore.GREEN + f"VALID: {username}" + Style.RESET_ALL)
            war = False  # Stop the loop
            with open("hits.txt", "w") as file:
                file.write(username)
            return True
        else:
            print(Fore.RED + f"{responseData.get('message')}: {username}" +
                  Style.RESET_ALL)
    except requests.exceptions.RequestException as e:
        print(Fore.YELLOW + f"glitch {username}: {e}" + Style.RESET_ALL)
    return False


print('Do you want to load usernames from a file?(yes/no)')
file = input().lower()
if file == 'yes':
    while True:
        with open("usernames.txt", "r") as file:
            usernames = file.read().splitlines()
        for username in usernames:
            checkUsername(username)
            time.sleep(0.05)
else:
    print('How many letters do you want it to be?')
    num = int(input().strip())

    print('Do you want it to have numbers? (yes/no)')
    nums = input().strip().lower()

    print(
        'Do you want it to repeat or randomize? If so, say how many; otherwise, just type no'
    )
    repeatVar = input().strip()

    # Define character set
    if nums == 'yes':
        characters = string.ascii_lowercase + string.digits
    else:
        characters = string.ascii_lowercase

    # Generate all possible combinations
    fourLetterCombinations = [
        ''.join(comb) for comb in itertools.product(characters, repeat=num)
    ]

    # Decide how many usernames to check
    if repeatVar != 'no':
        repeatCount = int(repeatVar)
        new = random.sample(fourLetterCombinations,
                            repeatCount)  # Pick usernames ONCE
    else:
        repeatCount = 1

    while war:  # Run until a valid username is found
        if repeatVar == "no":
            new = random.sample(fourLetterCombinations,
                                1)  # Only randomize if user said "no"

        for username in new:
            if checkUsername(username):  # Stop if a valid username is found
                break



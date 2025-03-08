import itertools
import string
import random
import requests
from colorama import Fore, Style, init
from plyer import notification

init()
war = True
notification.notify(
    title="Hello!",
    message="This is a test notification",
    timeout=10
)

def checkUsername(username):
    global war
    url = f"https://auth.roblox.com/v1/usernames/validate?Username={username}&Birthday=2000-01-01"
    try:
        result = requests.get(url)
        responseData = result.json()
        code = responseData.get("code")
        if code == 0:
            print(Fore.GREEN + f"VALID: {username}" + Style.RESET_ALL)
            notification.notify(
                title="FOUND",
                message="USERNAME FOUND",
                timeout=10
            )
            war = False
        else:
            print(Fore.RED + f"{responseData.get('message')}: {username}" + Style.RESET_ALL)
    except requests.exceptions.RequestException as e:
        print(Fore.YELLOW + f"glitch {username}: {e}" + Style.RESET_ALL)
    return False

print('Do you want to check it sorted? (yes/no) (for now you can only choose no or else it will break)')
everyUsername = input().strip().lower()

print('How many letters do you want it to be?')
num = int(input().strip())

print('Do you want it to have numbers? (yes/no)')
nums = input().strip().lower()

if nums == 'yes':
    characters = string.ascii_lowercase + string.digits
else:
    characters = string.ascii_lowercase

fourLetterCombinations = [''.join(comb) for comb in itertools.product(characters, repeat=num)]

if everyUsername == 'no':
    new = random.sample(fourLetterCombinations, 1)
else:
    new = fourLetterCombinations
while True:
    for username in new:
        checkUsername(username)
        if war:
            break
    if everyUsername == 'no':
        new = random.sample(fourLetterCombinations, 1)








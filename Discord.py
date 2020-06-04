from colorama import Fore, init, Style
import requests
import random
import ctypes
import time
import os

ctypes.windll.kernel32.SetConsoleTitleW('Discord Status Changer | Developed by jokers')
init(convert=True, autoreset=True)
SuccessCounter = 0
ErrorCounter = 0
os.system('cls')

print(Fore.GREEN + '\n[' + Fore.WHITE + Style.BRIGHT + '1' + Style.RESET_ALL + Fore.GREEN + '] ' + Fore.WHITE + Style.BRIGHT + 'Text')
print(Fore.GREEN + '[' + Fore.WHITE + Style.BRIGHT + '2' + Style.RESET_ALL + Fore.GREEN + '] ' + Fore.WHITE + Style.BRIGHT + 'Text including emoji')
try:
    option = int(input(Fore.GREEN + '\n> ' + Fore.WHITE + Style.BRIGHT))
except ValueError as e:
    print(' ')
    print(Fore.RED + '[ERROR] ' + Fore.WHITE + Style.BRIGHT + str(e))
    input()
    quit()
if option == 1:
    os.system('cls')
    print(Fore.WHITE + Style.BRIGHT + '\nToken:')
    token = str(input(Fore.GREEN + '> ' + Fore.WHITE + Style.BRIGHT))
    print(' ')
    def ChangeStatus():
        global SuccessCounter
        global ErrorCounter
        try:
            session = requests.Session()
            headers = {
                'authorization': token,
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.306 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36',
                'content-type': 'application/json'
            }
            text = random.choice(['Hello world!', '123', 'abc'])
            data = '{"custom_status":{"text":"' + text + '"}}'
            r = session.patch('https://discordapp.com/api/v6/users/@me/settings', headers=headers, data=data)
            if '"custom_status": {"text": "' in r.text:
                print(Fore.GREEN + '[SUCCESS] ' + Fore.WHITE + Style.BRIGHT + 'Status changed: ' + str(text))
                SuccessCounter += 1
                ctypes.windll.kernel32.SetConsoleTitleW('Discord Status Changer | Success: ' + str(SuccessCounter) + ' | Errors: ' + str(ErrorCounter))
            else:
               print(r.text)
        except:
            pass
        time.sleep(1)
    while True:
        ChangeStatus()
elif option == 2:
    os.system('cls')
    print(Fore.WHITE + Style.BRIGHT + '\nToken:')
    token = str(input(Fore.GREEN + '> ' + Fore.WHITE + Style.BRIGHT))
    print(Fore.WHITE + Style.BRIGHT + '\nEmoji name:')
    EmojiName = str(input(Fore.GREEN + '> ' + Fore.WHITE + Style.BRIGHT))
    print(Fore.WHITE + Style.BRIGHT + '\nEmoji ID:')
    try:
        EmojiID = int(input(Fore.GREEN + '> ' + Fore.WHITE + Style.BRIGHT))
    except ValueError as e:
        print(' ')
        print(Fore.RED + '[ERROR] ' + Fore.WHITE + Style.BRIGHT + str(e))
        input()
        quit()
    print(' ')
    def ChangeStatus():
        global SuccessCounter
        global ErrorCounter
        try:
            session = requests.Session()
            headers = {
                'authorization': token,
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.306 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36',
                'content-type': 'application/json'
            }
            text = random.choice(['Hello world!', '123', 'abc'])
            data = '{"custom_status":{"text":"' + text + '","emoji_id":"' + str(EmojiID) + '","emoji_name":"' + str(EmojiName) + '"}}'
            r = session.patch('https://discordapp.com/api/v6/users/@me/settings', headers=headers, data=data)
            if 'custom_status' in r.text:
                print(Fore.GREEN + '[SUCCESS] ' + Fore.WHITE + Style.BRIGHT + 'Status changed: ' + str(text))
                SuccessCounter += 1
                ctypes.windll.kernel32.SetConsoleTitleW('Discord Status Changer | Success: ' + str(SuccessCounter) + ' | Errors: ' + str(ErrorCounter))
            else:
                print(r.text)
        except:
            pass
        time.sleep(1)
    while True:
        ChangeStatus()

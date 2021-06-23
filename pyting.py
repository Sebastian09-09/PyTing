import WConio2 as WConio
from colorama import init, Fore, Back, Style
import time
import sys
import os
import random
init(convert=True)
os.system('')
def move(y, x):
    print("\033[%d;%dH" % (y, x))

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
       os.system('clear')

def main():
    print(Style.DIM)
    print(Fore.YELLOW + '''
█▀█ █▄█ ▀█▀ █ █▄░█ █▀▀
█▀▀ ░█░ ░█░ █ █░▀█ █▄█\n\nTest your Typing skills in the Terminal!!''')
    os.system("title "+"PyTing")
    quotes = []
    with open('assets/quotes.txt') as f:
        x = f.readlines()
        quotes.append(x)
        
    print(Style.BRIGHT)
    text = random.choice(quotes)
    text = (text[random.randint(0 , len(text))].replace('\n' , '')).replace('"', '' , 2) 
    ww = 0
    tw = len(text)
    time.sleep(1)
    os.system("title "+"PyTing - start typing now")
    word = len(text.split())
    move(8 , 1)
    print(Fore.MAGENTA + text)
    move(8 , 1)
    n_text = {}
    start = time.time()
    i = 0
    while True:
        try:
            key = WConio.getkey()
            if key == text[i]:
                sys.stdout.write(Fore.GREEN + key)
                sys.stdout.flush()
                
                if i not in n_text:
                    n_text[i] = key
                i += 1
                if len(text) == i:
                        break
                    
            else:
                if text[i] == ' ':
                    n_text[i] = f'~{key}~'
                    ww += 1
                else:
                    n_text[i] = f'~{key}~'
                    ww += 1               
                pass   
        except IndexError:
            break
    end = time.time()
    total_time = end - start
    print('\n')
    for i in n_text:
        if n_text[i].startswith('~'):
            print(Back.RED + n_text[i].replace('~', '' , 2) , end='')
            
        else:
            print(Fore.GREEN + n_text[i] , end='')
        print(Back.RESET , end='')
    print()
    print(Fore.MAGENTA + f'-->You made {ww} mistake/mistakes')
    print(f'-->Accuracy {100 - ((ww/tw)*100)}%')
    print(f'-->Your Typing Speed is {word * 60 / total_time} WPM')

if __name__ == '__main__':
    while True:
        x = input(Fore.YELLOW + 'Type \'y\' to start and \'n\' to end [y/n] : ')
        if x.lower() == 'y':
            clear()
            main()
            input(Fore.RED + 'press enter to continue')
            clear()
        else:
            break

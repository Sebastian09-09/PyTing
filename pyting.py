import WConio2 as WConio
import time
import sys
from os import system
from colorama import init, Fore, Back, Style
import random
init(convert=True)
print(Style.DIM)
print(Fore.YELLOW + '''
█▀█ █▄█ ▀█▀ █ █▄░█ █▀▀
█▀▀ ░█░ ░█░ █ █░▀█ █▄█\n\nTest your Typing skills in the Terminal!!''')
system("title "+"PyTing")
def move(y, x):
    print("\033[%d;%dH" % (y, x))

quotes = []
with open('assets/quotes.txt') as f:
    x = f.readlines()
    quotes.append(x)
    
print(Style.BRIGHT)
time.sleep(1)
system("title "+"PyTing - start typing now")
text = random.choice(quotes)
text = (text[random.randint(0 , len(text))].replace('\n' , ''))
ww = 0
tw = len(text)
print(Fore.MAGENTA + text)
word = len(text.split())
move(7 , 1)

def main():
    global ww
    global tw
    global word
    global text
    n_text = {}
    start = time.time()
    i = 0
    while True:
        try:
            key = WConio.getkey()
            if key == text[i]:
                if text[i] == ' ':
                    sys.stdout.write(Fore.GREEN + '_')
                    sys.stdout.flush()
                else:
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
    print(f'-->You Scored {100 - ((ww/tw)*100)}%')
    print(f'-->Your Typing Speed is {word * 60 / total_time} WPM')
    input(Fore.RED + 'Press ENTER to QUIT')

if __name__ == '__main__':
    main()
    print(random())

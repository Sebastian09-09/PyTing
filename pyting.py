import WConio2 as WConio
from colorama import init, Fore, Back, Style
import time
import sys
import os
import random
init(convert=True)
os.system('')

def main():
    print(Style.DIM)
    print(Fore.YELLOW + '''
█▀█ █▄█ ▀█▀ █ █▄░█ █▀▀
█▀▀ ░█░ ░█░ █ █░▀█ █▄█\n\nTest your Typing skills in the Terminal!!''')
    quotes = []
    with open('assets/quotes.txt') as f:
        x = f.readlines()
        quotes.append(x)
        
    print(Style.BRIGHT)
    text = random.choice(quotes)
    text1 = (text[random.randint(0 , len(text))].replace('\n' , '')).replace('"', '' , 2)
    text2 = (text[random.randint(0 , len(text))].replace('\n' , '')).replace('"', '' , 2)
    text3 = (text[random.randint(0 , len(text))].replace('\n' , '')).replace('"', '' , 2)
    text = text1 + ' ' +text2 + ' ' +text3 #single text is too small
    ww = 0
    tw = len(text)
    cont = False
    temp = []
    for i in range(-3  , 0):
        os.system("title "+f"PyTing {abs(i)}")
        print(str(abs(i)) , end='\r')
        time.sleep(.8)
    os.system("title "+"PyTing - start typing now")
    word = len(text.split())
    WConio.gotoxy(0, 7)
    print(Fore.MAGENTA + text)
    WConio.gotoxy(0, 7)
    n_text = {}
    start = time.time()
    i = 0
    while True:
        try:
            key = WConio.getch()

            if key[0] == 27:
                pass
                
            if key[0] == ord(text[i]):
                if text[i] == ' ':
                    cont = False
                    temp = []
                if cont == False:
                    sys.stdout.write(Fore.GREEN + key[1])
                    sys.stdout.flush()
                else:
                    sys.stdout.write(Fore.CYAN + key[1])
                    sys.stdout.flush()
                    n_text[i] = f'`{key[0]}`'
                    ww += 1
                
                n_text[i] = key[0]

                i += 1
                if len(text) == i:
                    break

            elif key[0] == 8 and i != 0 and text[i] != ' ':
                x = WConio.wherex()
                y = WConio.wherey()
                WConio.gotoxy(x-1, y)
                print(Fore.MAGENTA + text[i-1] , end='')
                print(Fore.GREEN , end='')
                x = WConio.wherex()
                WConio.gotoxy(x-1, y)
                try:
                    temp.remove(i-1)
                except:
                    pass
                if i-1 in n_text:
                    try:
                        if n_text[i-1].startswith('~'):
                            cont = False
                    except:
                        pass

                if temp != []:
                    cont = True
                i -= 1
                    
            else:
                if i != 0:
                    if text[i] == ' ':
                        sys.stdout.write(text[i])
                        sys.stdout.flush()
                        n_text[i] = '~32~'
                        cont = True
                        temp = []
                    
                    else:
                        sys.stdout.write(Fore.RED + text[i])
                        sys.stdout.flush()
                        n_text[i] = f'~{key[0]}~'
                        ww += 1
                        cont = True
                        temp.append(i)

                    i += 1
                    if len(text) == i:
                        break

        except IndexError:
            break
    end = time.time()
    total_time = end - start
    print('\n')
    for i in n_text:
        if str(n_text[i]).startswith('`'):
            x = n_text[i].replace('`', '' , 2)
            print(Back.CYAN + chr(int(x)) , end='')
        elif str(n_text[i]).startswith('~'):
            x = n_text[i].replace('~', '' , 2)
            print(Back.RED + chr(int(x)) , end='')
        else:
            print(Fore.GREEN + chr(int(n_text[i])) , end='')
        print(Back.RESET , end='')
    print()
    print(Fore.MAGENTA + f'-->You made {ww} mistake/mistakes')
    print(f'-->Accuracy {100 - ((ww/tw)*100)}%')
    print(f'-->Your Typing Speed is {word * 60 / total_time} WPM')

if __name__ == '__main__':
    os.system("title "+"PyTing")
    while True:
        x = input(Fore.RED + 'Type \'y\' to start and \'n\' to end [y/n] : ')
        if x.lower() == 'y':
            WConio.clrscr()
            main()
            input(Fore.RED + 'press enter to continue ')
            WConio.clrscr()
            os.system("title "+"PyTing")

        else:
            break
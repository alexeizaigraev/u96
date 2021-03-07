
import os
import sys
import tech

from priem import *
from otpusk import *
from perevod import *
from postall import *
from terminals import *
from sitenew import *
from summury import *
from natasha import *
from monitor import *
from accback import *
from walker import *

def mk_menu(kv):
    #os.system('cls')
    print()
    init()
    my_keys = list(kv.keys())
    num = 0
    p_green('\n' + '_' * 75 + '\n')
    for point in kv:
        num += 1
        #p_yellow(f'\t{num} {point}')
        print(f'{Fore.CYAN}\t{num} {point}', end = "\t")

    choice = -1
    while choice != 0:
        print(f'{Fore.GREEN}\n\n -> ', end='')
        choice = input()
        if '' == choice:
            menu_main()
        elif 0 < int(choice) < len(my_keys) + 1:
            comand = 'python ' + kv[my_keys[int(choice)-1]] + '.py'
            os.system('cls')
            os.system(comand)
            mk_menu(kv)
        elif '0' == choice:
            sys.exit()
        else:
            print(f'{Fore.RED} >> wrong choice!')


def menu_main():
    os.system('cls')
    MenuBody = '\n\n 1 People    2 Some    3 Monitors     4 Kabinet     5 Base'
    p_cyan(MenuBody)
        
    choise = -1
    while choise != 0:
        print('\n\n -> ', end='')
        choise = input()
        
        if "1"  == choise:
            os.system('cls')
            menu_people()

        if "2"  == choise:
            os.system('cls')
            menu_some()

        if "3"  == choise:
            os.system('cls')
            menu_monitor()

        if "4"  == choise:
            os.system('cls')
            menu_kabinet()

        if "5"  == choise:
            os.system('cls')
            menu_base()

        elif '0' == choise:
            sys.exit()
        else:
            print('\n\twrong choise!')

def menu_people():
    
    MenuBody = '\n\n\t1 Priem    2 Otpusk    3 Perevod     4 PostAll'
    p_cyan(MenuBody)

    choise = -1
    while choise != 0:
        print('\n\n -> ', end='')
        choise = input().strip()
        if '' == choise:
            menu_main()
        
        elif '1' == choise:
            os.system('cls')
            u = Priem()
            u.priem_main()
            menu_people()
        
        elif '2' == choise:
            os.system('cls')
            u = Otpusk()
            u.otpusk_main()
            menu_people()

        elif '3' == choise:
            os.system('cls')
            u = Perevod()
            u.perevod_main()
            menu_people()
        
        elif '4' == choise:
            os.system('cls')
            u = Postall()
            u.postall_main()
            menu_people()

        elif '0' == choise:
            sys.exit()
        else:
            print('\n\twrong choise!')

def menu_some():
    MenuBody = '\n\n\t1 Terminals    2 Site    3 Summury     4 Nanasha'
    p_cyan(MenuBody)

    choise = -1
    while choise != 0:
        print('\n\n -> ', end='')
        choise = input().strip()
        if '' == choise:
            menu_main()
        
        elif '1' == choise:
            os.system('cls')
            u = Terminals()
            u.terminals_main()
            menu_some()
        
        elif '2' == choise:
            os.system('cls')
            u = Site()
            u.site_main()
            menu_some()

        elif '3' == choise:
            os.system('cls')
            u = Summury()
            u.summury_main()
            menu_some()

        elif '4' == choise:
            os.system('cls')
            u = Natasha()
            u.natasha_main()
            menu_some()

        elif '0' == choise:
            sys.exit()
        else:
            p_red('\n\twrong choise!')


def menu_monitor():
    MenuBody = '\n\n\t1 Monitor    2 AccBack    3 Walker'
    p_cyan(MenuBody)

    choise = -1
    while choise != 0:
        print('\n\n -> ', end='')
        choise = input().strip()
        if '' == choise:
            menu_main()
        
        elif '1' == choise:
            os.system('cls')
            u = Monitor()
            u.monitor_main()
            menu_monitor()
        
        elif '2' == choise:
            os.system('cls')
            u = Accback()
            u.accback_main()
            menu_monitor()

        elif '3' == choise:
            os.system('cls')
            u = Walker()
            u.walker_main()
            menu_monitor()
        

        elif '0' == choise:
            sys.exit()
        else:
            p_red('\n\twrong choise!')

def menu_kabinet():
    h_kabinet = {'Knigi': 'knigi',
                 'Rro': 'rro',
                 'Pereezd': 'pereezd',
                 'Otmena': 'otmena',
                 'OtmenaKnigi': 'otmena_knigi',}
    os.system('cls')
    mk_menu(h_kabinet)

def menu_base():
    h_base = {'add_otbor': 'add_otbor',
            'add_vsyo_zapros': 'add_vsyo_zapros',}
    os.system('cls')
    mk_menu(h_base)



init()
menu_main()

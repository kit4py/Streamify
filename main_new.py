# file to rule them all :)

import os
import time
import sys

from user_input import NUM_OF_RUNNING_WINDOWS, USE_NORD_VPN, USE_MOUSE_DONT_SLEEP
from delete_inactive_user import delete_users, delete_user_chrome, clear_txt, all_usr_chrome, count_users_left, USERS_IN_TXT
from remake_input_data import input_data
# from stream_new1 import USER_COUNT_SN_1
# from stream_new2 import USER_COUNT_SN_2
# from stream_new3 import USER_COUNT_SN_3


def logo():
    print(BCOLORS.GREEN_LOGO + '''
    ███████╗████████╗██████╗ ███████╗ █████╗ ███╗   ███╗██╗███████╗██╗   ██╗
    ██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔══██╗████╗ ████║██║██╔════╝╚██╗ ██╔╝
    ███████╗   ██║   ██████╔╝█████╗  ███████║██╔████╔██║██║█████╗   ╚████╔╝ 
    ╚════██║   ██║   ██╔══██╗██╔══╝  ██╔══██║██║╚██╔╝██║██║██╔══╝    ╚██╔╝  
    ███████║   ██║   ██║  ██║███████╗██║  ██║██║ ╚═╝ ██║██║██║        ██║   
    ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝        ╚═╝   

                                                 ''' + BCOLORS.ENDC)


def start_count_main():
    print(f"\r" + '\033[93m' + '[+] Starting ' + '\033[94m' + '\033[1m' + 'STREAMIFY' + '\033[0m', end="")
    time.sleep(0.5)
    print(f"\r" + '\033[93m' + '[+] Starting ' + '\033[94m' + '\033[1m' + 'STREAMIFY.' + '\033[0m', end="")
    sys.stdout.flush()
    time.sleep(0.5)
    print(f"\r" + '\033[93m' + '[+] Starting ' + '\033[94m' + '\033[1m' + 'STREAMIFY..' + '\033[0m', end="")
    sys.stdout.flush()
    time.sleep(0.5)
    print(f"\r" + '\033[93m' + '[+] Starting ' + '\033[94m' + '\033[1m' + 'STREAMIFY...' + '\033[0m'+'\n', end="")
    sys.stdout.flush()


def go():
    # num_of_windows = int(input(ALL_COLOR + 'Number of open windows (1-4): ' + END_COLOR))
    num_of_windows = NUM_OF_RUNNING_WINDOWS
    list_commands = []
    for num in range(num_of_windows):
        list_commands.append(f'python3 stream_new{num + 1}.py & ')
    # nord_vpn = input(ALL_COLOR + 'Use NordVPN Y/n: ' + END_COLOR)
    # move_mous = input('Move mouse every 30s to not sleep Y/n: ')
    nord_vpn = USE_NORD_VPN
    move_mous = USE_MOUSE_DONT_SLEEP
    if nord_vpn is True:
        list_commands.append('python3 nord_rotate.py & ')
        print('\033[93m' + '[+] Running NordVPN...' + '\033[0m')
    if move_mous is True:
        list_commands.append('python3 mouse_dont_sleep.py & ')
        print('\033[93m' + '[+] Running MouseDontSleep...' + '\033[0m')
    else:
        print('\033[93m' + '[-] MouseDontSleep NOT Running' + '\033[0m' + '\n')

    list_commands.append('wait')

    a = (''.join(list_commands))
    # print(a)
    start_count_main()
    print('')
    os.system(a)


def reg():
    # num_of_windows = int(input(ALL_COLOR + 'Number of open windows (1-4): ' + END_COLOR))
    num_of_windows = NUM_OF_RUNNING_WINDOWS
    list_commands = []
    for num in range(num_of_windows):
        list_commands.append(f'python3 register.py & ')
    # nord_vpn = input(ALL_COLOR + 'Use NordVPN Y/n: ' + END_COLOR)
    # move_mous = input('Move mouse every 30s to not sleep Y/n: ')
    nord_vpn = USE_NORD_VPN
    move_mous = USE_MOUSE_DONT_SLEEP
    if nord_vpn is True:
        list_commands.append('python3 nord_rotate.py & ')
        print('\033[93m' + '[+] Running NordVPN...' + '\033[0m')
    if move_mous is True:
        list_commands.append('python3 mouse_dont_sleep.py & ')
        print('\033[93m' + '[+] Running MouseDontSleep...' + '\033[0m')
    else:
        print('\033[93m' + '[-] MouseDontSleep NOT Running' + '\033[0m' + '\n')

    list_commands.append('wait')

    a = (''.join(list_commands))
    # print(a)
    print('')
    os.system(a)


def reg_go():
    # num_of_windows = int(input(ALL_COLOR + 'Number of open windows (1-4): ' + END_COLOR))
    num_of_windows = NUM_OF_RUNNING_WINDOWS
    list_commands = []
    for num in range(num_of_windows):
        list_commands.append(f'python3 reg_play{num + 1}.py & ')
    # nord_vpn = input(ALL_COLOR + 'Use NordVPN Y/n: ' + END_COLOR)
    # move_mous = input('Move mouse every 30s to not sleep Y/n: ')
    nord_vpn = USE_NORD_VPN
    move_mous = USE_MOUSE_DONT_SLEEP
    if nord_vpn is True:
        list_commands.append('python3 nord_rotate.py & ')
        print('\033[93m' + '[+] Running NordVPN...' + '\033[0m')
    if move_mous is True:
        list_commands.append('python3 mouse_dont_sleep.py & ')
        print('\033[93m' + '[+] Running MouseDontSleep...' + '\033[0m')
    else:
        print('\033[93m' + '[-] MouseDontSleep NOT Running' + '\033[0m' + '\n')

    list_commands.append('wait')

    a = (''.join(list_commands))
    # print(a)
    start_count_main()
    print('')
    os.system(a)


def func_del_users():
    print('\033[93m' + '[!] Deleting Banned/Inactive Accounts...' + '\033[0m')
    delete_users()
    delete_user_chrome()
    clear_txt()
    all_usr_chrome()  # delete if folder left, not used
    count_users_left()
    print('\033[93m' + f'[+] Accounts Deleted Successfully' + '\033[0m' + '\n')
    print(BCOLORS.GREEN_LOGO + f'[+] {len(USERS_IN_TXT)} Accounts Left' + BCOLORS.ENDC + '\n')


def total_usr_count():
    pass
    # total_count = USER_COUNT_SN_1 + USER_COUNT_SN_2 + USER_COUNT_SN_3
    # print('\n' + '\033[94m' + '\033[1m' + f''' -- USER COUNT: {total_count} --''' + '\033[0m' + '\n' + '\n')


class BCOLORS:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[39m'
    GREEN_LOGO = '\033[94m' + '\033[1m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


ALL_COLOR = BCOLORS.OKGREEN
END_COLOR = BCOLORS.ENDC


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    logo()
    # time.sleep(1000)
    func_del_users()
    input_data()

    task = int(input('\033[93m' + '''Choose task:
[1] play 
[2] create accounts  
[3] create & play  
Enter number: '''+'\033[0m'))
    print('')

    if task == 1:
        go()
    elif task == 2:
        reg()
    elif task == 3:
        reg_go()
    else:
        print('something went wrong')


# print(BCOLORS.GREEN_LOGO + '''
#    _____ __                            _ ____
#   / ___// /_________  ____ _____ ___  (_) __/_  __
#   \__ \/ __/ ___/ _ \/ __ `/ __ `__ \/ / /_/ / / /
#  ___/ / /_/ /  /  __/ /_/ / / / / / / / __/ /_/ /
# /____/\__/_/   \___/\__,_/_/ /_/ /_/_/_/  \__, /
#                                          /____/
#                                          ''' + BCOLORS.ENDC)

# proxy-server:socks5 ip port
# undeet.chormedriver.v2

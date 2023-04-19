import csv
import shutil
import time
import os
import re
import glob


from resources.pathes import CHROME_PROFILES


USERS_IN_TXT = []


def count_users_left():
    with open('./resources/dataOG.txt', mode='r') as dt:
        reader = csv.reader(dt)
        for row in reader:
            USERS_IN_TXT.append(row)
    dt.close()


def delete_users():
    list_to_remove = []
    # load users to delete and append to list to delete
    with open('./resources/DATADELETE.txt', mode='r+') as dt:
        reader = csv.reader(dt)
        for row in reader:
            a = ''.join(row)
            list_to_remove.append(a)
    dt.close()

    # print(list_to_remove)

    new_list = []
    # compare og data with to_delete > create new list, with working users
    with open('./resources/dataOG.txt', mode='r+') as fp:
        reader = csv.reader(fp)
        for row in reader:
            b = ''.join(row)
            if b not in list_to_remove:
                new_list.append(b)
    fp.close()
    # write new list in the main user file
    with open('./resources/dataOG.txt', mode='w') as dg:
        for item in new_list:
            # print(item)
            dg.write(item + '\n')
    dg.close()


def delete_user_chrome():
    list_to_remove_chrome = []
    # load users to delete and append to list to delete
    with open('./resources/DATADELETE.txt', mode='r') as dt:
        reader = csv.reader(dt)
        for row in reader:
            a = ''.join(row)
            username = re.split(':', a)[0]
            list_to_remove_chrome.append(username)
    dt.close()

    # print(list_to_remove_chrome)  # list of users to be deleted

    for user in list_to_remove_chrome:
        path = f'{CHROME_PROFILES}{user}'
        if os.path.exists(path):
            try:
                shutil.rmtree(path)
            except:
                pass
            try:
                os.rmdir(path)
            except:
                pass
            print(f'[+] User deleted: {user}')
        else:
            print('\033[91m'+f'[-] User NOT deleted!: {user}'+'\033[0m')


def all_usr_chrome():
    all_user = []
    # load users to delete and append to list to delete
    with open('./resources/dataOG.txt', mode='r') as dt:
        reader = csv.reader(dt)
        for row in reader:
            a = ''.join(row)
            username = re.split(':', a)[0]
            all_user.append(username)
    dt.close()
    # print(all_user)
    # print(len(all_user))
    # print('all users in txt')

    all_usr_dir = glob.glob(CHROME_PROFILES + '*')
    reformat_usr_dir = []

    for user in all_usr_dir:
        a = (''.join(user))
        a = re.split('/', a)[6]
        reformat_usr_dir.append(a)
        # time.sleep(1)

    # print(reformat_usr_dir)
    # print(len(reformat_usr_dir))
    # print('all users in directory')
    test_list = []

    for u in reformat_usr_dir:
        if u not in all_user:
            path = f'{CHROME_PROFILES}{u}'
            if os.path.exists(path):
                # print(u + 'NOT EXISTEND')
                test_list.append(u)

                try:
                    shutil.rmtree(path)
                except:
                    pass
                try:
                    os.rmdir(path)
                except:
                    pass
                print(f'[+] User deleted: {u}')


def clear_txt():
    # clear DATADELETE.txt
    with open('./resources/DATADELETE.txt', mode='w') as dtf:
        dtf.write('')
    dtf.close()


if __name__ == '__main__':
    count_users_left()
    print(len(USERS_IN_TXT))

    # all_usr_chrome()
    # delete_users()
    # delete_user_chrome()
    # clear_txt()

import undetected_chromedriver as uc
from undetected_chromedriver import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time
import random
import math
from datetime import datetime, date
import os
import re
import csv

from resources.agents_sizes import user_agents_desktop, window_sizes_desktop, user_agents_mobile, window_sizes_mobile, window_desk_test
from resources.pathes import CHROME_PROFILES, DRIVER_PATH, USER_FOLDER, USER_LIST_TXT_PATH, CHROME_PROFILES_REGISTER
from resources.add_ons import TODAY_DATE, NOW_TIME
from resources.links import LINKS_TO_PLAY
from user_input import TASK_FIRST, NUMBER_SKIP, MAX_PLAY_TIME, MIN_PLAY_TIME, FOLLOW_SAVE_VAR
import resources.pathes as p
import user_input


class SpotifyBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        options = ChromeOptions()
        options.add_argument(f"--window-size=900,900")
        options.add_argument(f'--user-agent={random.choice(user_agents_desktop)}')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument("--disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--password-store=basic")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-extensions")
        options.add_argument("--enable-automation")
        options.add_argument("--disable-browser-side-navigation")
        options.add_argument("--disable-web-security")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument("--disable-software-rasterizer")

        options.add_argument(f"--user-data-dir={CHROME_PROFILES}{username}")
        # options.add_argument('--proxy-server=85.195.81.151:12971')
        options.add_argument(f'--proxy-server=https://85.195.81.151:12971')

        # options.add_argument("--incognito")
        # options.add_argument('--headless')
        # options.headless = True
        s = Service(
            executable_path=DRIVER_PATH)
        self.browser = uc.Chrome(service=s, options=options, use_subprocess=True)
        self.wait = WebDriverWait(self.browser, user_input.WEBSITE_LOAD_TIME)
        self.wait_follow = WebDriverWait(self.browser, 3)

    def test_wait(self):
        browser = self.browser
        wait = self.wait
        browser.get('https://open.spotify.com/artist/6LuN9FCkKOj5PcnpouEgny')
        time.sleep(1)
        browser.get('https://google.com')
        wait.until(EC.visibility_of_element_located((By.XPATH, p.PLAY_ARTIST_XPATH1))).click()
        # print('wait function didnt work')

        time.sleep(1000)

    def close_browser(self):
        self.browser.close()
        self.browser.quit()

    def login(self, user_line):
        browser = self.browser
        browser.get('https://open.spotify.com/')
        time.sleep(random.randrange(3, 5))

        xpath1 = '//*[@id="main"]/div/div[2]/div[1]/header/div[5]/button[2]/span'
        xpath2 = '/html/body/div[3]/div/div[2]/div[1]/header/div[5]/button[2]/span'

        if self.xpath_exists(xpath1 or xpath2):
            print('[-] Not Logged in, trying to login')
            browser.get('https://accounts.spotify.com/login')
            time.sleep(random.randrange(5, 7))

            self.get_cookie_at_login()

            username_input = browser.find_element(by=By.ID, value='login-username')
            username_input.clear()
            username_input.send_keys(username)
            time.sleep(random.randrange(1, 2))

            password_input = browser.find_element(by=By.ID, value='login-password')
            password_input.clear()
            password_input.send_keys(password)
            time.sleep(random.randrange(1, 3))

            password_input.send_keys(Keys.ENTER)
            time.sleep(random.randrange(11, 14))

            browser.get('https://open.spotify.com/')

            time.sleep(3)
            self.get_cookie_at_login()

            if self.xpath_exists(xpath1 or xpath2):
                print(f'[-] NOT LOGGED IN!')

                user_to_delete_list.append(user_line)
                with open('./resources/DATADELETE.txt', mode='a') as fps:
                    a = ''.join(user_line)
                    fps.write(str(a + '\n'))
                    print(a)
                fps.close()
            else:
                print(f'[+] Logged in!')
        else:
            print('[+] Logged in!')

    def get_cookie_at_login(self):
        browser = self.browser
        try:
            browser.find_element(By.ID, 'onetrust-accept-btn-handler').click()
            time.sleep(random.randrange(1, 2))
        except:
            pass

    # look if element on page with XPATH
    def xpath_exists(self, url):
        browser = self.browser
        try:
            browser.find_element(by=By.XPATH, value=url)
            exist = True
        except NoSuchElementException:
            exist = False
        return exist

    def partial_link_text(self, url):
        browser = self.browser
        try:
            browser.find_element(by=By.PARTIAL_LINK_TEXT, value=url)
            exist = True
        except NoSuchElementException:
            exist = False
        return exist

    def skip_forward(self, play_time):
        browser = self.browser
        xpath1 = '//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[2]/button[1]'
        xpath2 = '/html/body/div[4]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[2]/button[1]'

        if self.xpath_exists(xpath1):
            self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath1))).click()
            time.sleep(play_time)
        if self.xpath_exists(xpath2):
            self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath2))).click()
            time.sleep(play_time)
        else:
            print('[-] could not skip')

    def skip_back(self, play_time):
        browser = self.browser
        xpath1 = '//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[1]/button[2]'
        xpath2 = '/html/body/div[4]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[1]/button[2]'

        if self.xpath_exists(xpath1):
            browser.find_element(by=By.XPATH, value=xpath1).click()
            time.sleep(play_time)
        if self.xpath_exists(xpath2):
            browser.find_element(by=By.XPATH, value=xpath1).click()
            time.sleep(play_time)
        else:
            print('[-] could not skip')

    def play(self, play_time, skip_number):
        browser = self.browser
        try:
            for link in LINKS_TO_PLAY:
                browser.get(link)
                # time.sleep(random.randrange(8, 12))
                a = (''.join(link))
                a = re.split('/', a)[3]
                print(f'processing {a}: {link}')

                if a == 'artist':
                    self.wait.until(EC.visibility_of_element_located((By.XPATH, p.PLAY_ARTIST_XPATH1))).click()
                    time.sleep(random.randrange(1, 2))
                    # time.sleep(1000)

                    # follow/save
                    if FOLLOW_SAVE_VAR is True:
                        try:
                            browser.find_element(By.XPATH, p.FOLLOW_ARTIST_XPATH1).click()
                        except:
                            print('[-] could not follow/save!!!')
                    if skip_number > 0:
                        for number in range(skip_number):
                            self.skip_forward(play_time)
                        print(f'[+] played {number} songs, each {play_time}')
                    elif skip_number <= 0:
                        time.sleep(play_time)
                        print(f'[+] played: {play_time} sec')

                    else:
                        print(f'[-] WRONG XPATH! {username}')

                if a == 'playlist':
                    self.wait.until(EC.visibility_of_element_located((By.XPATH, p.PLAY_PLAYLIST_XPATH1))).click()
                    time.sleep(random.randrange(1, 2))
                    if FOLLOW_SAVE_VAR is True:
                        try:
                            browser.find_element(By.XPATH, p.SAVE_PLAYLIST_XPATH1).click()
                        except:
                            print('[-] could not follow/save!!!')
                    # skip method
                    if skip_number > 0:
                        for number in range(skip_number):
                            self.skip_forward(play_time)
                        print(f'[+] played {number} songs, each {play_time}')
                    elif skip_number <= 0:
                        time.sleep(play_time)
                        print(f'[+] played: {play_time} sec')
                    else:
                        print(f'[-] WRONG XPATH! {username}')

                if a == 'track':
                    self.wait.until(EC.visibility_of_element_located((By.XPATH, p.PLAY_SONG_XPATH1))).click()
                    time.sleep(random.randrange(1, 2))
                    if FOLLOW_SAVE_VAR is True:
                        try:
                            browser.find_element(By.XPATH, p.SAVE_PLAYLIST_XPATH1).click()
                        except:
                            print('[-] could not follow/save!!!')
                    # skip method
                    if skip_number > 0:
                        for number in range(skip_number):
                            self.skip_forward(play_time)
                        print(f'[+] played {number} songs, each {play_time}')
                    elif skip_number <= 0:
                        time.sleep(play_time)
                        print(f'[+] played: {play_time} sec')
                    else:
                        print(f'[-] WRONG XPATH! {username}')

                if a == 'album':
                    self.wait.until(EC.visibility_of_element_located((By.XPATH, p.PLAY_ALBUM_XPATH1))).click()
                    time.sleep(random.randrange(1, 2))
                    if FOLLOW_SAVE_VAR is True:
                        try:
                            browser.find_element(By.XPATH, p.SAVE_ALBUM_XPATH1).click()
                        except:
                            print('[-] could not follow/save!!!')
                    # skip method
                    if skip_number > 0:
                        for number in range(skip_number):
                            self.skip_forward(play_time)
                        print(f'[+] played {number} songs, each {play_time}')
                    elif skip_number <= 0:
                        time.sleep(play_time)
                        print(f'[+] played: {play_time} sec')
                    else:
                        print(f'[-] WRONG XPATH! {username}')

                if a == 'user':
                    if FOLLOW_SAVE_VAR is True:
                        self.wait.until(EC.visibility_of_element_located((By.XPATH, p.FOLLOW_USER_XPATH1))).click()
                        time.sleep(random.randrange(1, 2))
                    else:
                        print(f'[-] could not follow!!! {username}')
        except:
            print('\033[91m' + '[-] process interrupted' + '\033[0m')

    def test_profile(self):
        browser = self.browser
        browser.get('https://myip.com')
        time.sleep(10)
        browser.get('https://nowsecure.nl')
        time.sleep(10)
        browser.get('https://distilnetworks.com')
        time.sleep(10)
        browser.get('https://myuseragent.com')
        time.sleep(1000)


if __name__ == '__main__':

    start = time.time()

    taskFirst = TASK_FIRST

    if taskFirst == 0:
        time.sleep(user_input.USER_START_SLEEP * 3)
        user_count = 0
        with open('./resources/dataOG.txt', mode='r') as fp:
            reader = csv.reader(fp, delimiter=',')
            line = 0
            for row in reader:
                line += 1
                # where to start in the user list >
                if user_input.STREAM4_MAX_USER_NUM + 1 > line > user_input.STREAM3_MAX_USER_NUM:
                    try:
                        b = ''.join(row)
                        # print(b)
                        username = re.split(':', b)[0]
                        print(f'[+] User: ' + username)
                        password = re.split(':', b)[1]
                        # print(password)

                        # time.sleep(0.5)
                        my_bot = SpotifyBot(username, password)
                        # my_bot.testik()
                        # song_play_time = random.randrange(MIN_PLAY_TIME, MAX_PLAY_TIME)
                        #
                        # my_bot = SpotifyBot(username, password)
                        my_bot.login()
                        # my_bot.play(song_play_time, NUMBER_SKIP)
                        time.sleep(random.randrange(1, 2))
                        my_bot.close_browser()
                        time.sleep(random.randrange(1, 2))
                        user_count += 1
                        print('\033[93m' + f'[...] {user_count} user(s) finished' + '\033[0m' + '\n')

                    except Exception as ex:
                        print(ex)
            print('\n' + '\033[94m' + '\033[1m' + f''' -- USER COUNT: {user_count} --''' + '\033[0m' + '\n' + '\n')
    # direct play
    if taskFirst == 1:
        time.sleep(user_input.USER_START_SLEEP * 3)
        user_count = 0
        with open(USER_LIST_TXT_PATH, mode='r') as fp:
            reader = csv.reader(fp, delimiter=',')
            line = 0
            for row in reader:
                line += 1
                # where to start in the user list >
                if user_input.STREAM4_MAX_USER_NUM + 1 > line > user_input.STREAM3_MAX_USER_NUM:
                    try:
                        b = ''.join(row)
                        # print(b)
                        username = re.split(':', b)[0]
                        print(f'[+] User: ' + username)
                        password = re.split(':', b)[1]
                        # print(password)

                        song_play_time = random.randrange(MIN_PLAY_TIME, MAX_PLAY_TIME)

                        my_bot = SpotifyBot(username, password)
                        # my_bot.login()
                        my_bot.play(song_play_time, NUMBER_SKIP)
                        time.sleep(random.randrange(1, 2))
                        my_bot.close_browser()
                        time.sleep(random.randrange(1, 2))
                        user_count += 1
                        print('\033[93m'+f'[...] {user_count} user(s) finished' + '\033[0m' + '\n')

                    except Exception as ex:
                        print(ex)
                        raise
            print('\n' + '\033[94m' + '\033[1m' + f''' -- USER COUNT: {user_count} --''' + '\033[0m' + '\n' + '\n')
    # with login
    if taskFirst == 2:
        time.sleep(user_input.USER_START_SLEEP * 3)
        user_count = 0
        with open(USER_LIST_TXT_PATH, mode='r') as fp:
            reader = csv.reader(fp, delimiter=',')
            line = 0
            for row in reader:
                line += 1
                # where to start in the user list >
                if user_input.STREAM4_MAX_USER_NUM + 1 > line > user_input.STREAM3_MAX_USER_NUM:
                    try:
                        b = ''.join(row)
                        # print(b)
                        username = re.split(':', b)[0]
                        print(f'[+] User: ' + username)
                        password = re.split(':', b)[1]
                        # print(password)

                        song_play_time = random.randrange(MIN_PLAY_TIME, MAX_PLAY_TIME)

                        my_bot = SpotifyBot(username, password)
                        my_bot.login(b)
                        my_bot.play(song_play_time, NUMBER_SKIP)
                        time.sleep(random.randrange(1, 2))
                        my_bot.close_browser()
                        time.sleep(random.randrange(1, 2))
                        user_count += 1
                        print('\033[93m'+f'[...] {user_count} user(s) finished' + '\033[0m' + '\n')

                    except Exception as ex:
                        print(ex)
                        raise
            print('\n' + '\033[94m' + '\033[1m' + f''' -- USER COUNT: {user_count} --''' + '\033[0m' + '\n' + '\n')
    else:
        print(f'Wrong number! Try again!')

    end = time.time()
    time_used = end - start
    time_used_sec = int(math.ceil(time_used))
    print(f'Time used {time_used_sec} second(s)')
    time_used_minutes = time_used_sec / 60
    print(f'Time used {round(time_used_minutes)} minute(s)')

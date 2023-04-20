import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from resources.dataOG import users_settings_dict
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time
import random
import math
from datetime import datetime, date
import os
import re

from resources.agents_sizes import user_agents_desktop, window_sizes_desktop, user_agents_mobile, window_sizes_mobile, window_desk_test
from resources.pathes import CHROME_PROFILES, DRIVER_PATH, USER_FOLDER
from resources.add_ons import TODAY_DATE, NOW_TIME
from resources.links import LINKS_TO_PLAY
from user_input import TASK_FIRST, NUMBER_SKIP, MAX_PLAY_TIME, MIN_PLAY_TIME


class SpotifyBot:

    def __init__(self, username, password, window_size, user_agent):
        self.username = username
        self.password = password
        options = Options()
        options.add_argument(f"--window-size={random.choice(window_desk_test)}")
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
        # options.add_argument("--incognito")
        # options.add_argument('--headless')
        # options.headless = True
        s = Service(
            executable_path=DRIVER_PATH)
        self.browser = uc.Chrome(service=s, options=options)

    def print_users(self):
        pass

    def close_browser(self):
        self.browser.close()
        self.browser.quit()

    def login(self):
        file_user = f'{USER_FOLDER}{username}/'
        file_today = f'{USER_FOLDER}{username}/{TODAY_DATE}/'

        def create_user_folder():
            if not os.path.exists(file_user):
                os.mkdir(file_user)

        def create_today_folder():
            if not os.path.exists(file_today):
                os.mkdir(file_today)

        create_user_folder()
        create_today_folder()

        browser = self.browser
        browser.get('https://open.spotify.com/')
        time.sleep(random.randrange(3, 5))

        xpath1 = '//*[@id="main"]/div/div[2]/div[1]/header/div[5]/button[2]/span'
        xpath2 = '/html/body/div[3]/div/div[2]/div[1]/header/div[5]/button[2]/span'

        if self.xpath_exists(xpath1 or xpath2):
            print('[-] Not Logged in, trying to login')
            browser.get('https://accounts.spotify.com/login')
            time.sleep(random.randrange(5, 7))

            # accept cookie
            def accept_cookie():
                try:
                    browser.find_element(By.ID, 'onetrust-accept-btn-handler').click()
                except:
                    pass

            accept_cookie()

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

            accept_cookie()
            print(f'[+] Logged in!')

        else:
            print('[+] Logged in!')

        now_time = datetime.now().strftime('%H-%M-%S')
        browser.save_screenshot(f'{USER_FOLDER}{username}/{TODAY_DATE}/{now_time}.jpg')

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
        finally:
            browser.save_screenshot(f'{USER_FOLDER}{username}/{TODAY_DATE}/{NOW_TIME}.jpg')
        return exist

    def partial_link_text(self, url):
        browser = self.browser
        try:
            browser.find_element(by=By.PARTIAL_LINK_TEXT, value=url)
            exist = True
        except NoSuchElementException:
            exist = False
        return exist

    def play_something(self, link, playtime):
        pass

    def skip_forward(self, play_time):
        browser = self.browser
        xpath1 = '//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[2]/button[1]'
        xpath2 = '/html/body/div[4]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[2]/button[1]'

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
        # forward
        # //*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[2]/button[1]
        # /html/body/div[4]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[2]/button[1]

        # back
        # //*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[1]/button[2]
        # /html/body/div[4]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[1]/button[2]

        print(f'processing: {LINKS_TO_PLAY}')

        for link in LINKS_TO_PLAY:
            browser.get(link)
            time.sleep(random.randrange(8, 12))

            a = (''.join(link))
            a = re.split('/', a)[3]
            print(f'playing {a}: {link}')

            if a == 'artist':
                xpath1 = '/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div/div[2]/div[2]/div[4]/div/div/div/div/div/button'
                xpath2 = '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div/div[2]/div[2]/div[4]/div/div/div/div/div/button'
                xpath3 = '/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div/div[2]/div[2]/div[4]/div/div/div/div/div/button'  # same as 1

                now_time = datetime.now().strftime('%H-%M-%S')
                browser.save_screenshot(f'{USER_FOLDER}{username}/{TODAY_DATE}/{now_time}.jpg')

                if self.xpath_exists(xpath1):
                    browser.find_element(by=By.XPATH, value=xpath1).click()
                    if skip_number > 0:
                        for number in range(skip_number):
                            self.skip_forward(play_time)
                        print(f'[+] played {number} songs, each {play_time}')
                    elif skip_number <= 0:
                        time.sleep(play_time)
                        print(f'[+] played: {play_time} sec')
                    now_time = datetime.now().strftime('%H-%M-%S')
                    browser.save_screenshot(f'{USER_FOLDER}{username}/{TODAY_DATE}/{now_time}.jpg')

                elif self.xpath_exists(xpath2):
                    browser.find_element(by=By.XPATH, value=xpath2).click()
                    time.sleep(play_time)
                    print(f'[+] played: {play_time} sec')
                    now_time = datetime.now().strftime('%H-%M-%S')
                    browser.save_screenshot(f'{USER_FOLDER}{username}/{TODAY_DATE}/{now_time}.jpg')

                elif self.xpath_exists(xpath3):
                    browser.find_element(by=By.XPATH, value=xpath3).click()
                    time.sleep(play_time)
                    print(f'[+] played: {play_time} sec')
                    now_time = datetime.now().strftime('%H-%M-%S')
                    browser.save_screenshot(f'{USER_FOLDER}{username}/{TODAY_DATE}/{now_time}.jpg')

                else:
                    print(f'[-] WRONG XPATH! {username}')
                    now_time = datetime.now().strftime('%H-%M-%S')
                    browser.save_screenshot(f'{USER_FOLDER}{username}/{TODAY_DATE}/{now_time}.jpg')

            if a == 'playlist':
                xpath1 = '/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[1]/section/div[2]/div[2]/div[4]/div/div/div/div/div/button'
                xpath2 = '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[1]/section/div[2]/div[2]/div[4]/div/div/div/div/div/button'

                now_time = datetime.now().strftime('%H-%M-%S')
                browser.save_screenshot(f'{USER_FOLDER}{username}/{TODAY_DATE}/{now_time}.jpg')

                if self.xpath_exists(xpath1):
                    browser.find_element(by=By.XPATH, value=xpath1).click()
                    time.sleep(play_time)
                    print(f'[+] played: {play_time} sec')
                    now_time = datetime.now().strftime('%H-%M-%S')
                    browser.save_screenshot(f'{USER_FOLDER}{username}/{TODAY_DATE}/{now_time}.jpg')

                elif self.xpath_exists(xpath2):
                    browser.find_element(by=By.XPATH, value=xpath2).click()
                    time.sleep(play_time)
                    print(f'[+] played: {play_time} sec')
                    now_time = datetime.now().strftime('%H-%M-%S')
                    browser.save_screenshot(f'{USER_FOLDER}{username}/{TODAY_DATE}/{now_time}.jpg')

                else:
                    print(f'[-] WRONG XPATH! {username}')
                    now_time = datetime.now().strftime('%H-%M-%S')
                    browser.save_screenshot(f'{USER_FOLDER}{username}/{TODAY_DATE}/{now_time}.jpg')

            if a == 'song':
                xpath1 = '/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[3]/div[4]/div/div/div/div/div/button'
                xpath2 = '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[3]/div[4]/div/div/div/div/div/button'

                now_time = datetime.now().strftime('%H-%M-%S')
                browser.save_screenshot(f'{USER_FOLDER}{username}/{TODAY_DATE}/{now_time}.jpg')

                if self.xpath_exists(xpath1):
                    browser.find_element(by=By.XPATH, value=xpath1).click()
                    time.sleep(play_time)
                    print(f'[+] played: {play_time} sec')
                    now_time = datetime.now().strftime('%H-%M-%S')
                    browser.save_screenshot(f'{USER_FOLDER}{username}/{TODAY_DATE}/{now_time}.jpg')

                elif self.xpath_exists(xpath2):
                    browser.find_element(by=By.XPATH, value=xpath2).click()
                    time.sleep(play_time)
                    print(f'[+] played: {play_time} sec')
                    now_time = datetime.now().strftime('%H-%M-%S')
                    browser.save_screenshot(f'{USER_FOLDER}{username}/{TODAY_DATE}/{now_time}.jpg')

                else:
                    print(f'[-] WRONG XPATH! {username}')
                    now_time = datetime.now().strftime('%H-%M-%S')
                    browser.save_screenshot(f'{USER_FOLDER}{username}/{TODAY_DATE}/{now_time}.jpg')

            if a == 'album':
                xpath1 = '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[3]/div[4]/div/div/div/div/div/button'
                xpath2 = '/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[3]/div[4]/div/div/div/div/div/button'

                now_time = datetime.now().strftime('%H-%M-%S')
                browser.save_screenshot(f'{USER_FOLDER}{username}/{TODAY_DATE}/{now_time}.jpg')

                if self.xpath_exists(xpath1):
                    browser.find_element(by=By.XPATH, value=xpath1).click()
                    time.sleep(play_time)
                    print(f'[+] played: {play_time} sec')
                    now_time = datetime.now().strftime('%H-%M-%S')
                    browser.save_screenshot(f'{USER_FOLDER}{username}/{TODAY_DATE}/{now_time}.jpg')

                elif self.xpath_exists(xpath2):
                    browser.find_element(by=By.XPATH, value=xpath2).click()
                    time.sleep(play_time)
                    print(f'[+] played: {play_time} sec')
                    now_time = datetime.now().strftime('%H-%M-%S')
                    browser.save_screenshot(f'{USER_FOLDER}{username}/{TODAY_DATE}/{now_time}.jpg')

                else:
                    print(f'[-] WRONG XPATH! {username}')
                    now_time = datetime.now().strftime('%H-%M-%S')
                    browser.save_screenshot(f'{USER_FOLDER}{username}/{TODAY_DATE}/{now_time}.jpg')

if __name__ == '__main__':

    start = time.time()

    print('''
       _____ __                            _ ____     
      / ___// /_________  ____ _____ ___  (_) __/_  __
      \__ \/ __/ ___/ _ \/ __ `/ __ `__ \/ / /_/ / / /
     ___/ / /_/ /  /  __/ /_/ / / / / / / / __/ /_/ / 
    /____/\__/_/   \___/\__,_/_/ /_/ /_/_/_/  \__, /  
                                             /____/ ''')
    #
    # taskFirst = int(input('''
    # [0] test
    # [1] upcoming coming soon
    #
    # Enter number: '''))
    taskFirst = TASK_FIRST

    if taskFirst == 0:
        user_count = 0
        for user, user_data in users_settings_dict.items():
            try:
                username = user_data['login']
                password = user_data['password']
                window_size = user_data['window_size']
                user_agent = user_data['user_agent']

                print(username + ':' + password)
                # time.sleep(1)
                #
                # song_play_time = random.randrange(MIN_PLAY_TIME, MAX_PLAY_TIME)
                #
                # my_bot = SpotifyBot(username, password, window_size, user_agent)
                # my_bot.login()
                # my_bot.play(song_play_time, NUMBER_SKIP)
                # time.sleep(random.randrange(1, 2))
                # my_bot.close_browser()
                # time.sleep(random.randrange(1, 2))
                # user_count += 1
                # print(f'[...] {user_count} user(s) finished' + '\n')
            except Exception as ex:
                print(ex)
                print('[-] could not play')
                pass

        print(f'''
             -- USER COUNT: {user_count} -- 
                          ''')

    if taskFirst == 1:

        skip_num = int(input('Number of skips: '))

        link_play_time_min = int(input('minimum play time in sec: '))
        link_play_time_max = int(input('maximum play time in sec: '))

        user_count = 0

        for user, user_data in users_settings_dict.items():
            try:
                username = user_data['login']
                password = user_data['password']
                window_size = user_data['window_size']
                user_agent = user_data['user_agent']

                song_play_time = random.randrange(link_play_time_min, link_play_time_max)

                my_bot = SpotifyBot(username, password, window_size, user_agent)
                my_bot.login()
                my_bot.play(song_play_time, skip_num)
                time.sleep(random.randrange(1, 2))
                my_bot.close_browser()
                time.sleep(random.randrange(1, 2))
                user_count += 1
                print(f'[...] {user_count} user(s) finished' + '\n')
            except Exception as ex:
                print(ex)
                print('[-] could not play')

        print(f'''
             -- USER COUNT: {user_count} -- 
                          ''')

    else:
        print(f'Wrong number! Try again!')

    end = time.time()
    time_used = end - start
    time_used_sec = int(math.ceil(time_used))
    # print used time in sec
    print(f'Time used {time_used_sec} second(s)')
    time_used_minutes = time_used_sec / 60
    print(f'Time used {time_used_minutes} minute(s)')



#
# https://open.spotify.com/artist/4qcIzzD06n7i9eRJvanHLn
# https://open.spotify.com/album/7wAkGF3GhXygP25JXzCquq
# https://open.spotify.com/track/0NLi4JGjKDHD43yzXhjU6v
# https://open.spotify.com/track/1kvsJaqvnEXg31jsAjsicg
# https://open.spotify.com/track/0xhipNnj96krm7gnsQEor0
#
# Artists
# https://open.spotify.com/artist/7ncmqjrlT2WOxUl5dK3vrt
# https://open.spotify.com/artist/08TQdmnGF22nDGUcwbRG2E
# https://open.spotify.com/artist/4jErNKhzv5jQk61h8VWNFV
#
# Songs
# https://open.spotify.com/track/4vlotPDbcGmEbgJ2ljLpeq
# https://open.spotify.com/track/0XZpxgY2UZmM7OQAmJlVBu
# https://open.spotify.com/track/5Qbv6RV1gmewZE8wcEWAWa
#
# Playlist
# https://open.spotify.com/playlist/6HsVMz3LDvXUJ6oYUnPW5n
# https://open.spotify.com/playlist/37i9dQZF1DX6ZomwsYVLXI
# https://open.spotify.com/playlist/6oxtcww4Gbo0suJ4Z1eA34
#
# Album
# https://open.spotify.com/album/7M842DMhYVALrXsw3ty7B3
# https://open.spotify.com/album/5RtVpw3b2a0RKJ3Ab6qhNm
# https://open.spotify.com/album/1ZCh3BOpOEiU3FshszqJcg

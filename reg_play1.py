import undetected_chromedriver as uc
from selenium.webdriver.support.ui import Select
from resources.pathes import USER_LIST_TXT_PATH, USER_FOLDER, NEW_USER_REG_TXT1
import resources.agents_sizes as ags
from user_input import REGISTER_ACCOUNTS_QUANTITY
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time
import random
import re
import csv

from resources.pathes import CHROME_PROFILES, DRIVER_PATH, USER_FOLDER, USER_LIST_TXT_PATH, CHROME_PROFILES_REGISTER
from resources.links import LINKS_TO_PLAY
from user_input import TASK_FIRST, NUMBER_SKIP, MAX_PLAY_TIME, MIN_PLAY_TIME, FOLLOW_SAVE_VAR
import resources.pathes as p
import user_input


def generate():
    def gen_user():
        # Generate a random username
        username = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
        username += ''.join(random.choices('0123456789', k=3))
        username += ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=2))
        username += ''.join(random.choices('0123456789', k=1))
        username += random.choice(
            ['@hi2.in', '@telegmail.com', '@proton.me', '@gmail.com', '@dnmx.com', '@gmx.com', '@web.de'])

        # Generate a random password
        password = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8))
        final_user = username + ':' + password
        # print(final_user)
        user_file_txt.append(final_user)

    gen_count = REGISTER_ACCOUNTS_QUANTITY
    count = gen_count

    user_file_txt = []
    with open(NEW_USER_REG_TXT1, mode='w') as fp:
        for i in range(count):
            gen_user()
        a = ('\n'.join(user_file_txt))
        fp.write(a+'\n')
    fp.close()


class SpotifyBot:

    def __init__(self, username, password, name):
        self.username = username
        self.password = password
        self.name = name
        options = Options()

        proxy_list = [
            '196.19.176.39:8000'
        ]  # 196.19.176.39:8000
        # options.add_argument(f'--proxy-server=socks5://{random.choice(proxy_list)}')
        options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
        options.add_argument(f"--window-size={random.choice(ags.window_sizes_desktop)}")
        options.add_argument(f'--user-agent={random.choice(ags.user_agents_desktop)}')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument("--disable-extensions")
        # options.add_argument("--proxy-server='direct://'")
        options.add_argument(f"--proxy-bypass-list={proxy_list}")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--no-sandbox")
        # options.add_argument("--enable-automation")
        # options.add_argument("--disable-browser-side-navigation")
        # options.add_argument("--disable-web-security")
        # options.add_argument("--disable-dev-shm-usage")
        # options.add_argument("--disable-infobars")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument("--disable-software-rasterizer")

        options.add_argument(f"--user-data-dir={CHROME_PROFILES}{username}")
        s = Service(
            executable_path=DRIVER_PATH)
        self.browser = uc.Chrome(service=s, options=options)
        self.wait = WebDriverWait(self.browser, user_input.WEBSITE_LOAD_TIME)
        self.wait_follow = WebDriverWait(self.browser, 3)

    def test_proxy(self):
        browser = self.browser
        # browser.get('https://www.nowsecure.ln')
        # time.sleep(10)
        browser.get('https://www.myip.com')
        time.sleep(5)
        # browser.get('http://whoer.net/')
        # time.sleep(5)

    def close_browser(self):
        self.browser.close()
        self.browser.quit()

    def get_cookie_at_login(self):
        browser = self.browser
        try:
            browser.find_element(By.ID, 'onetrust-close-btn-container').click()
        except:
            pass
        try:
            browser.find_element(By.ID, 'onetrust-accept-btn-handler').click()
        except:
            pass

    def login(self):
        browser = self.browser
        # CODE TO LOG IN AND GET COOKIE TO FILE
        browser.get('https://www.spotify.com/signup')
        time.sleep(random.randrange(2, 3))

        self.get_cookie_at_login()
        browser.delete_all_cookies()
        time.sleep(1)

        # paste email
        print(f'''[+] Registration started...''')
        username_input = browser.find_element(by=By.ID, value='email')
        # username_input = browser.find_element(by=By.ID, value='email')
        username_input.clear()
        username_input.send_keys(username)
        time.sleep(3)
        #
        self.get_cookie_at_login()
        # paste email again
        password_input = browser.find_element(by=By.ID, value='confirm')
        password_input.clear()
        password_input.send_keys(username)
        time.sleep(2)
        self.get_cookie_at_login()
        # paste password
        password_input = browser.find_element(by=By.ID, value='password')
        password_input.clear()
        password_input.send_keys(password)
        time.sleep(2)
        self.get_cookie_at_login()
        # paste name
        password_input = browser.find_element(by=By.ID, value='displayname')
        password_input.clear()
        password_input.send_keys(name)
        time.sleep(2)
        self.get_cookie_at_login()
        # paste day
        password_input = browser.find_element(by=By.ID, value='day')
        password_input.clear()
        password_input.send_keys(str(random.randrange(1, 28)))
        time.sleep(2)
        self.get_cookie_at_login()
        # paste month
        all_month = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober',
                     'November', 'Dezember']
        all_month_num = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        password_input = Select(browser.find_element(by=By.ID, value='month'))
        password_input.select_by_value(random.choice(all_month_num))
        time.sleep(2)
        self.get_cookie_at_login()
        # paste year
        password_input = browser.find_element(by=By.ID, value='year')
        password_input.clear()
        password_input.send_keys(str(random.randrange(1996, 2006)))
        time.sleep(2)
        self.get_cookie_at_login()
        # paste gender
        random_gender = random.randrange(1, 3)
        if random_gender == 1:
            # paste name
            browser.find_element(by=By.XPATH, value='/html/body/div[1]/main/div/div/form/fieldset/div/div[1]/label/span[1]').click()
            time.sleep(2)

        elif random_gender == 2:
            browser.find_element(by=By.XPATH, value='/html/body/div[1]/main/div/div/form/fieldset/div/div[2]/label/span[1]').click()
            time.sleep(2)

        else:
            browser.find_element(by=By.XPATH, value='/html/body/div[1]/main/div/div/form/fieldset/div/div[5]/label/span[1]').click()
            time.sleep(2)
        self.get_cookie_at_login()
        # check box (share reg for marketing purposes)
        try:
            browser.find_element(by=By.XPATH, value='/html/body/div[1]/main/div/div/form/div[7]/div/label/span[1]').click()
            time.sleep(2)

        except:
            pass
        # check box (agree to terms of use)
        self.get_cookie_at_login()
        try:
            browser.find_element(by=By.XPATH, value='/html/body/div[1]/main/div/div/form/div[8]/div/label/span[1]').click()
            time.sleep(2)
        except:
            pass
        # REGISTER
        self.get_cookie_at_login()
        try:
            browser.find_element(by=By.XPATH, value=p.XPATH_GERMANY).click()
        except:
            pass
        try:
            browser.find_element(by=By.XPATH, value=p.XPATH_SWITZERLAND).click()
        except:
            pass
        try:
            browser.find_element(by=By.XPATH, value=p.XPATH_USA).click()
        except:
            pass
        # time.sleep(random.randrange(7, 9))
        # time.sleep(1000)

        # register Btn
        try:
            browser.find_element(By.XPATH, p.XPATH_GERMANY_FINAL).click()
        except:
            pass
        try:
            browser.find_element(By.XPATH, p.XPATH_USA_FINAL).click()
        except:
            pass
        time.sleep(random.randrange(7, 9))
        self.get_cookie_at_login()

        # final confirm button
        try:
            browser.find_element(By.XPATH, p.XPATH_USA_REG).click()
            # print('found button conf')
        except:
            pass
            # print('not btn confr')
        time.sleep(random.randrange(13, 14))

        # download link confirm
        try:
            browser.find_element(By.PARTIAL_LINK_TEXT, 'Herunterladen')
            print(f'[+] User: {username} created successfully!')
        except:
            pass
        try:
            browser.find_element(By.PARTIAL_LINK_TEXT, 'Download')
            print(f'[+] User: {username} created successfully!')
        except:
            pass
        # print(f'[+] User: {username} created successfully!')
        # time.sleep(1000)

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
        for link in LINKS_TO_PLAY:
            try:
                browser.get(link)
                time.sleep(random.randrange(1, 2))
                a = (''.join(link))
                a = re.split('/', a)[3]
                print(f'processing {a}: {link}')
                self.get_cookie_at_login()

                if a == 'artist':
                    self.wait.until(EC.visibility_of_element_located((By.XPATH, p.PLAY_ARTIST_XPATH1))).click()
                    time.sleep(random.randrange(1, 2))
                    # follow/save
                    self.get_cookie_at_login()
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
                    self.get_cookie_at_login()
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
                    self.get_cookie_at_login()
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
                    self.get_cookie_at_login()
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
                        self.get_cookie_at_login()
                        self.wait.until(EC.visibility_of_element_located((By.XPATH, p.FOLLOW_USER_XPATH1))).click()
                        time.sleep(random.randrange(1, 2))
                    else:
                        print(f'[-] could not follow!!! {username}')
            except Exception as ex2:
                print(ex2)
                print('\033[91m' + '[-] process interrupted' + '\033[0m')
                continue

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


user_to_delete_list = []


if __name__ == '__main__':

    generate()

    user_count = 0

    with open(NEW_USER_REG_TXT1, mode='r') as fp:
        reader = csv.reader(fp, delimiter=',')
        for row in reader:
            try:
                print('registering...')
                b = ''.join(row)
                print(b)
                username = re.split(':', b)[0]
                print(username)
                password = re.split(':', b)[1]
                print(password)
                name = random.choice(ags.first_names)
                print(name)

                song_play_time = random.randrange(MIN_PLAY_TIME, MAX_PLAY_TIME)
                # song_play_time = 400

                my_bot = SpotifyBot(username, password, name)
                # my_bot.test_proxy()
                # time.sleep(1000)
                try:
                    my_bot.login()
                    with open('./resources/dataOG.txt', mode='a') as fr:
                        fr.write('\n' + b)
                    fr.close()
                    my_bot.play(song_play_time, NUMBER_SKIP)
                    my_bot.close_browser()
                except:
                    print('[-] something went wrong')
                    my_bot.close_browser()

                user_count += 1
                print('\033[93m' + f'[...] {user_count} user(s) finished' + '\033[0m' + '\n')

            except Exception as ex:
                print(ex)

        print('\n' + '\033[94m' + '\033[1m' + f''' -- USER COUNT: {user_count} --''' + '\033[0m' + '\n')

    fp.close()

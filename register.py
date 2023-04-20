import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import random
import time
import csv
import re
import os

from resources.pathes import USER_LIST_TXT_PATH, USER_FOLDER, NEW_USER_REG_TXT1
import resources.agents_sizes as ags
from resources.pathes import CHROME_PROFILES, DRIVER_PATH, USER_FOLDER
from resources.add_ons import TODAY_DATE, NOW_TIME
from user_input import REGISTER_ACCOUNTS_QUANTITY


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
        options.add_argument(f"--window-size={random.choice(ags.window_sizes_mobile)}")
        options.add_argument(f'--user-agent={random.choice(ags.user_agents_mobile)}')
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
        s = Service(
            executable_path=DRIVER_PATH)
        self.browser = uc.Chrome(service=s, options=options)
        self.wait = WebDriverWait(self.browser, 30)
        self.wait_follow = WebDriverWait(self.browser, 3)

    def close_browser(self):
        self.browser.close()
        self.browser.quit()

    def get_cookie_at_login(self):
        browser = self.browser
        try:
            browser.find_element(By.ID, 'onetrust-accept-btn-handler').click()
            time.sleep(random.randrange(1, 2))
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
        username_input = self.wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        # username_input = browser.find_element(by=By.ID, value='email')
        username_input.clear()
        username_input.send_keys(username)
        time.sleep(2)
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
        browser.find_element(by=By.XPATH, value='/html/body/div[1]/main/div/div/form/div[7]/div/label/span[1]').click()
        time.sleep(2)
        self.get_cookie_at_login()
        # check box (agree to terms of use)
        browser.find_element(by=By.XPATH, value='/html/body/div[1]/main/div/div/form/div[8]/div/label/span[1]').click()
        time.sleep(2)
        self.get_cookie_at_login()
        # REGISTER
        browser.find_element(by=By.XPATH, value='/html/body/div[1]/main/div/div/form/div[9]/div/button').click()
        # time.sleep(random.randrange(7, 9))

        # Confirm Reg> Create Acc

        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div/div/div[2]/main/div/div/div/div/div/button'))).click()
        # browser.find_element(by=By.XPATH, value='/html/body/div/div/div[2]/main/div/div/div/div/div/button').click()
        time.sleep(2)
        self.get_cookie_at_login()
        self.wait.until(EC.visibility_of_element_located(
            (By.PARTIAL_LINK_TEXT, 'Herunterladen')))
        print(f'[+] User: {username} created successfully!')


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

                my_bot = SpotifyBot(username, password, name)
                try:
                    my_bot.login()
                    with open('./resources/dataOG.txt', mode='a') as fr:
                        fr.write('\n' + b)
                    fr.close()
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

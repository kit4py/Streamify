
import pyautogui as pa
import time
import os

nord_count = 1000

# print('[+] nordVPN running...')
# print('\033[93m'+'[+] Running NordVPN...'+'\033[0m')

def runNord():
    time.sleep(nord_count)

    os.system("open /Applications/NordVPN.app")
    time.sleep(0.3)
    pa.moveTo(x=1659, y=1028)
    pa.click()
    # time.sleep(0.3)
    # pa.click()

x = 0

while True:
    runNord()
    x += 1
    print(f'Nord Switched {x} times!')



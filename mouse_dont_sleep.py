
import pyautogui as pa
import time

# sec_count = int(input('Enter minutes to stay awake: '))
sec_count = 2000
sec_count = sec_count * 60
# print(f'This is {str(sec_count)} seconds!')
# print('[+] mouse moving every 30s...')
# print('\033[93m'+'[+] Running MouseDontSleep...'+'\033[0m')

for i in range(sec_count):
    pa.moveTo(x=700, y=800)
    # print(f'Mouse moved 30 passed')
    time.sleep(30)
    pa.moveTo(x=800, y=800)
    # print('fMouse moved another 30 seconds passed')
    time.sleep(30)


import os
import platform
import subprocess
import time


def input_data():
    filepath = './resources/links.txt'
    file = 'user_input.txt'
    py_file = 'user_input.py'

    if platform.system() == 'Darwin':  # macOS
        subprocess.call(('open', file))
        time.sleep(0.5)
        subprocess.call(('open', filepath))
    elif platform.system() == 'Windows':  # Windows
        os.startfile(filepath)
        os.startfile(file)
    else:  # linux
        subprocess.call(('xdg-open', filepath))
        subprocess.call(('xdg-open', file))

    x = input('\033[93m'+'press [ENTER] to continue'+'\033[0m')

    with open(file, mode='r') as fr:
        x = fr.readlines()
        print(x)
        with open(py_file, mode='w') as fw:
            fw.writelines(x)


if __name__ == '__main__':
    input_data()
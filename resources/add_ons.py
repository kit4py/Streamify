from datetime import datetime, date

TODAY_DATE = str(date.today())
NOW_TIME = datetime.now().strftime('%H-%M-%S')

if __name__ == '__main__':
    print(TODAY_DATE)
    print(NOW_TIME)
# links
import csv
from resources.pathes import LINK_TXT_PATH

LINKS_TO_PLAY = []

with open(LINK_TXT_PATH, mode='r') as fp:
    reader = csv.reader(fp, delimiter=',')
    for row in reader:
        LINKS_TO_PLAY.append(', '.join(row))
fp.close()

if __name__ == '__main__':
    print(LINKS_TO_PLAY)

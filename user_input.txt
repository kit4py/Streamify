# input data to be used when playing links

# [0] test
# [1] direct play
# [2] check if logged in, then play
TASK_FIRST = 2

# If registering accounts => Quantity:
REGISTER_ACCOUNTS_QUANTITY = 80

# time allowed to wait, until website loads
WEBSITE_LOAD_TIME = 45

# time between window start
USER_START_SLEEP = 90

# number of skips for each playable link
NUMBER_SKIP = 0

# follow/save playlist True/False
FOLLOW_SAVE_VAR = True

# PLAY TIME: for each link!!! time * links = total time for 1 acc
# minimum play time
MIN_PLAY_TIME = 40
# maximum play time
MAX_PLAY_TIME = 60

# use NordVPN at the bottom right corner > True/False
USE_NORD_VPN = False

# use MouseMove each 30s to not fall a sleep and break code > True/False
USE_MOUSE_DONT_SLEEP = True

# running 4 windows, divide all users/window count (max 4)
NUM_OF_RUNNING_WINDOWS = 1
# >> if 4 windows running:
STREAM_START_NUM = 0
STREAM1_MAX_USER_NUM = 20   # window1 plays from 1-40 user in list
STREAM2_MAX_USER_NUM = 40  # window2 plays from 41-80 user in list
STREAM3_MAX_USER_NUM = 60  # window3 plays from 81-120 user in list
STREAM4_MAX_USER_NUM = 80  # window4 plays from 121-160 user in list

# >> if 3 windows running: EXAMPLE
# STREAM_START_NUM = 0
# STREAM1_MAX_USER_NUM = 50
# STREAM2_MAX_USER_NUM = 100
# STREAM3_MAX_USER_NUM = 150


import argparse
import time
from datetime import datetime
from datetime import timedelta
import os
import sys

def getArgs(argv=None):
    rules = "Remember:\n- No task larger than 5 pomodoros .\n- Any interruption = restart the pomodoro."
    parser = argparse.ArgumentParser(description="Pomodoro Timer with various \
            length of pomodor", epilog=rules)
    parser.add_argument('-s','--standard', action='store_true', default=True,
            help='25 min work, 5 min break\tDEFAULT')
    parser.add_argument('-b','--buster', action='store_true', default=False,
            help='10 min work, 2 min break')
    parser.add_argument('-g','--golden', action='store_true', default=False,
            help='50 min work, 15 min break')
    parser.add_argument('-bu','--busy', action='store_true', default=False,
            help='90 min work, 30 min break')
    return parser.parse_args(argv)


def pomodori_msg(pomodoro):
    msg = 'notify-send "BREAK ⏳ Timer done! Take a coffee break! ☕ 🍩 \
pomodoro {}/{}"'.format(pomodoro + 1, 4)
    return msg

def break_msg():
    msg = 'notify-send "WORK ⏳ Timer done! Back to work!"'
    return msg

def format_times(time):
    return time.isoformat(timespec="seconds")

def timer():
    running = True
    start = datetime.now()
    end = format_times(datetime.time(start + timedelta(minutes = TIME)))
    start = format_times(datetime.time(start))
    print("start {}, end {}".format(start, end))
    while running:
        now = format_times(datetime.time(datetime.now()))
        print("{}\r".format(now), end="", flush=True)
        if end == now:
            running = False 
        else:
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                print("Goodbye")
                sys.exit(0)

def main(TIME, BREAK):
    for pomodori in range(0,3):
        print("Pomodoro {}/{} ".format(pomodori + 1, 4), end="")
        timer()
        os.system(pomodori_msg(pomodori))
        print("Break {} ".format(pomodori + 1), end="")
        timer()
        os.system(break_msg())


if __name__ == "__main__":
    #TIME = 25
    #BREAK= 5
    TIME = 1
    BREAK = 1
    args = getArgs()
    if args.buster:
        TIME = 10
        BREAK = 2
    elif args.golden:
        TIME = 50
        BREAK = 15
    elif args.busy:
        TIME = 90
        BREAK = 30
    main(TIME, BREAK)

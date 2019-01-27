#!/usr/bin/env python3
import argparse
import time
from datetime import datetime
from datetime import timedelta
import os
import sys

def getArgs(argv=None):
    parser = argparse.ArgumentParser(description="Pomodoro Timer with various \
            length of pomodor")
    parser.add_argument('-s','--standard', action='store_true', default=True,
            help='25 min work, 5 min brk\tDEFAULT')
    parser.add_argument('-b','--buster', action='store_true', default=False,
            help='10 min work, 2 min brk')
    parser.add_argument('-g','--golden', action='store_true', default=False,
            help='50 min work, 15 min brk')
    parser.add_argument('-bu','--busy', action='store_true', default=False,
            help='90 min work, 30 min brk')
    return parser.parse_args(argv)


def pomodori_msg(pomodoro):
    msg = 'notify-send "brk ⏳ Timer done! Take a coffee brk! ☕ 🍩 \
pomodoro {}/{}"'.format(pomodoro + 1, 4)
    return msg

def brk_msg():
    msg = 'notify-send "WORK ⏳ Timer done! Back to work!"'
    return msg

def format_times(time_str):
    return time_str.isoformat(timespec="seconds")

def timer(run_time):
    running = True
    start = datetime.now()
    end = format_times(datetime.time(start + timedelta(minutes = run_time)))
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

def main(work, brk):
    print("Remember:\n- No task larger than 5 pomodori.\n\
- Any interruptions = restart the pomodoro.")
    for pomodori in range(0,3):
        print("Pomodoro {}/{} ".format(pomodori + 1, 4), end="")
        timer(work)
        os.system(pomodori_msg(pomodori))
        print("Break {} ".format(pomodori + 1), end="")
        timer(brk)
        os.system(brk_msg())


if __name__ == "__main__":
    work = 25
    brk= 5
    args = getArgs()
    if args.buster:
        work = 10
        brk = 2
    elif args.golden:
        work = 50
        brk = 15
    elif args.busy:
        work = 90
        brk = 30
    main(work, brk)

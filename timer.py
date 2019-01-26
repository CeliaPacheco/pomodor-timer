import argparse
import time
from datetime import datetime
from datetime import timedelta
import os

def getArgs(argv=None):
    rules = "Remember: \\
            - No task larger than 5 pomodoros.\\
            - Any interruption = restart the pomodoro."
    parser = argparse.ArgumentParser(description="Pomodoro Timer with various \
            length of pomodor", epilog=rules)
    parser.add_argument('-s','--standard', action='store_true', default=True,
            help='25 min work, 5 min break\tDEFAULT')
    parser.add_argument('-b','--buster', action='store_true', default=False,
            help='10 min work, 2 min break')
    parser.add_argument('-g','--golden', action='store_true', default=False,
            help='50 min work, 15 min break')
    parser.add_argument('-bu','--busy', action='store_true', defualt=False,
            help='90 min work, 30 min break')
    return parser.parse_args(argv)


class Buster:
    def __init__(self, start_time):
        self.start = start_time
        self.stop = 0
        _TIME = 10
        _SHORT_BREAK = 2
        _pomodori = 4

    def format_time(self):
        return time.isoformat(timespec="seconds")

    def stop_time(self):
        self.stop = datetime.time(self.start + timedelta(minutes = TIME)))

    def run(self)
       print("start {}, end {}".format(self.format_time(self.start), \
               self.format_time(self.stop))
       while _pomodori != 0:

            print("{}\r".format(self.format_time(datetime.time(datetime.now()))) \
                    end="", flush=True)


def format_times(time):
    return time.isoformat(timespec="seconds")


def main():
    RUNNING = True 
    TIME = 1 
    SHORT_BREAK = 5
    LONG_BREAK = 10

    #start = datetime.datetime.time((datetime.datetime.now()))
    start = datetime.now()
    end = format_times(datetime.time(start + timedelta(minutes = TIME)))
    start = format_times(datetime.time(start))
    print("start {}, end {}".format(start, end))

    while RUNNING:
        now = format_times(datetime.time(datetime.now()))
        print("{}\r".format(now), end="", flush=True)
        if end == now:
            RUNNING = False
        else:
            time.sleep(1)
    os.system('notify-send "⏳ Timer done! Take a coffee break! ☕ 🍩 :)"')
if __name__ == "__main__":
    args = getArgs()
    if args 


    main()

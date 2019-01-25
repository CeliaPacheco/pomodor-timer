import time
from datetime import datetime
from datetime import timedelta
import os


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

if __name__ == "__main__":
    main()

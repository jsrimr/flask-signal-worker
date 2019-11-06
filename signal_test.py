import signal
import sys
from time import sleep


def on_stop_handler(signum, frame):
    print('Exiting application...')
    sys.exit(0)


def listen_stop_signal():
    signal.signal(signal.SIGINT, on_stop_handler) #sigint : ctrl + c
    signal.signal(signal.SIGTERM, on_stop_handler) #sigterm : termination signal


def main_loop():
    listen_stop_signal()

    while True:
        sleep(1)
        print('Working...')

main_loop()
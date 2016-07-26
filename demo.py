#!/usr/bin/env python
import signal
import sys
def signal_handler(signal, frame):
    print('You ran "docker stop!"')
    sys.exit(0)
signal.signal(signal.SIGTERM, signal_handler)
print('Run "docker stop"!')
signal.pause()

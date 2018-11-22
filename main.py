# !/usr/bin/env python3
""" a simple script that periodically tests a bandwidth's speed. """
import time
import sys
import os
import argparse
from bandwidth_test import get_bandwidth_data
from logger import process_results


p = argparse.ArgumentParser()
p.add_argument('interval_minutes', nargs='?', const=1, type=int, default=15)
p.add_argument('debug', nargs='?', const=1, type=bool, default=False)
p.add_argument('single', nargs='?', const=1, type=bool, default=False)


# TODO: debug kwargs and their values
def main(interval_minutes, debug, single):
    """ Main function in module that will get bandwidth data periodically,
    until user decides to terminate program.
    Args:
        interval_minutes - set delay of running function in minutes
    Usage:
        Press CMD + C to terminate program.
    """
    print('Program starting! Standby . . . ')
    interval_seconds = 60 * interval_minutes
    try:
        while True:
            if debug:
                results = {'timestamp': '2018-11-22T02:34:07.415126Z',
                           'download': 6364856,
                           'upload': 2359296,
                           'ping': '22.227'
                           }
            else:
                results = get_bandwidth_data()
            process_results(results)
            if single == True:
                print('Single instance complete! exiting!')
                break
            time.sleep(interval_seconds)
    except KeyboardInterrupt:
        print('interrupted! Exiting now!')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


if __name__ == '__main__':
    args = p.parse_args()
    main(**vars(args))

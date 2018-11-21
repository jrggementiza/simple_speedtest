# !/usr/bin/env python3
""" a simple script that periodically tests a bandwidth's speed. """
import time, sys, os
from bandwidth_test import get_bandwidth_data


# TODO: refactor into own module that outputs logfiles into csv
def log_and_print(results_log):
    print(results_log)


# TODO: accept an interval for generating bandwidth data using sys.argv
def main(interval_minutes=15):
    """ Main function in module that will get bandwidth data periodically,
    until user decides to terminate program.
    Args:
        interval_minutes - set delay of running function in minutes
    Usage:
        Press CMD + C to terminate program.
    """
    interval_seconds = 60 * interval_minutes
    try:
        while True:
            results = get_bandwidth_data()
            log_and_print(results)
            time.sleep(interval_seconds)
    except KeyboardInterrupt:
        print('interrupted! Exiting now!')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


if __name__ == '__main__':
    main()

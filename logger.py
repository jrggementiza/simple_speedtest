# !/usr/bin/env python3
""" module that accepts a dictionary of bandwidth data, processes it, and
outputs a logfile in a txt file.
"""
import os
import datetime


# TODO: formatting, payload and use join on the return function
def log_and_print(timestamp, mbps_download, mbps_upload, ping):
    """ formats parameters into a payload to be printed and logged in a text file. """
    payload = f'timestamp: {timestamp} - download: {mbps_download:.2f} - upload: {mbps_upload:.2f} - ping: {ping}'
    print(payload)
    with open(f"{timestamp}"+".txt", "w") as f:
        f.write(payload+'\n')


def bit_to_mbps(bit):
    """ accepts a bit value returns its mbps value """
    MBPS_CONSTANT = 1048576
    return bit / MBPS_CONSTANT


# TODO: timestamp formatting. note: timestamp is a type str
def format_timestamp(timestamp):
    """ accepts a timestamp and formats it into a readable version """
    return timestamp


def process_results(results):
    """ Accepts a dictionary of bandwidth data and delegates
    processing to different subfunctions.
    """
    timestamp = format_timestamp(results['timestamp'])
    mbps_download = bit_to_mbps(results['download'])
    mbps_upload = bit_to_mbps(results['upload'])
    ping = results['ping']

    log_and_print(timestamp, mbps_download, mbps_upload, ping)


if __name__ == "__main__":
    process_results()

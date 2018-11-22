# !/usr/bin/env python3
""" bandwidth test is a module that handles the generation of bandwidth data
and processing of said data into a string format.
"""
import speedtest


def generate_bandwidth_data(st_object):
    """ Uses st_object to test and get the bandwidth's
    download and upload speeds.
    Args:
        st_object - an instance of the speedtest object
    Returns:
        results_dict - a dictionary of bandwidth data
    """
    st_object.download()
    st_object.upload()
    results_dict = st_object.results.dict()
    return results_dict


def initialize():
    """ Returns an instance of the speedtest object """
    return speedtest.Speedtest()


def get_bandwidth_data():
    """ Tests process, and returns a dict of bandwidth data """
    st_object = initialize()
    st_object.get_best_server()
    results_dict = generate_bandwidth_data(st_object)
    return results_dict


if __name__ == '__main__':
    get_bandwidth_data()

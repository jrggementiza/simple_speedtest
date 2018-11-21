# !/usr/bin/env python3
""" bandwidth test is a module that handles the generation of bandwidth data
and processing of said data into a string format.
"""

import speedtest


# TODO: formatting
def process_results_to_mbps(results):
    """ draft: accepts a dictionary, returns a formatted string for logging """
    MBPS_CONSTANT = 1048576

    timestamp = results['timestamp']
    print(type(timestamp))

    bit_download = results['download']
    bit_upload = results['upload']
    mbps_download = bit_download / MBPS_CONSTANT
    mbps_upload = bit_upload / MBPS_CONSTANT

    ping = results['ping']
    
    return f'timestamp: {timestamp} - download: {mbps_download:.2f} - upload: {mbps_upload:.2f} - ping: {ping}'
    

def generate_bandwidth_data(st_object):
    """ Uses st_object to test and get the bandwidth's download, upload, etc, speeds.
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
    """ Main function in module to test, process, and return a string of bandwidth data """
    st_object = initialize()
    st_object.get_best_server() # TODO: have option to save default server used
    results = generate_bandwidth_data(st_object)
    processed_results = process_results_to_mbps(results)
    return processed_results


if __name__ == '__main__':
    get_bandwidth_data()

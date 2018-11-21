# !/usr/bin/env python3
""" Accepts a dict and processes results for easy logging of 
download speed, upload speed, latency, and timestamp
"""

def get_processed_results(results):
    MBPS_CONSTANT = 1048576

    bit_download = results['download']
    bit_upload = results['upload']
    
    timestamp = results['timestamp']
    ping = results['ping']
    mbps_download = bit_download / MBPS_CONSTANT
    mbps_upload = bit_upload / MBPS_CONSTANT
    return timestamp, mbps_download, mbps_upload, ping

def main():
    pass # generate and print results one time    


if __name__ == '__main__':
    main()
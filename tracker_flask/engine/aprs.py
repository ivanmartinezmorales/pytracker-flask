import aprslib
import time
import logging

cols_to_keep = ['latitude', 'longitude', 'altitude', 'elevation', 'from']

def callback(packet):
    return packet


def connect_aprs(callsign, dwell_time=10):
    """
    This function connects to the APRS.fi server and returns the aprs
    connection to be used by the clean_data function.

    Added exception handling to test for stability.
    """
    aprs = aprslib.IS('0')
    aprs.set_server('rotate.aprs.net', 14580)
    aprs.filter = callsign
    aprs.connect()

    if aprs:

        # If aprs was successful, then tell the user that we connected
        print("successfully connected to aprs")
        # Return the aprs object
        return aprs

    else: # If you cannot connect, you must reconnect
        print("could not connect to aprs! check connection!")

def clean_data(aprs):
    """
    Function takes in the APRS object, then gathers a packet from
    aprs.consumer. This function will only gather one packet every time
    the function is called, that way we're not using two loops and
    increasing the run-time

    First thing, checking for aprs object. If there is one, then gather
    the packet. After gathering the packet, it will clean the packet up
    by getting rid of the values that we don't need, only leaving those
    that are in 'cols_to_keep'

    The funciton will return a dictionary, with the keys being 'cols_to_keep'
    and the values being the most recent packet values
    """

    # Checking for APRS object
    if aprs:

        # Gathering the packet from APRS
        packet = aprs.consumer(callback)

        # Cleaning the packet, first checking if the keys from
        # cols_to_keep actually exist within the packet

        while True:
            try:
                filtered_dict = {col: v for (col, v) in packet.items() if col in cols_to_keep}
                logging.info("dictionary filtered ok")
                return filtered_dict # returns dict
            except Exception as exp:
                logging.info("could not filter packet... retrying")
                time.sleep(2)
                break


def collect_data(callsign, dwell_time=10):
    """
    This function combines the two previous functions into one
    to be called in __init__.py. Callsign is passed into connect_aprs
    which generates the AIS object, allowing the use of the IS object from
    aprslib. It will return a packet every 10 seconds.

    rtype: dict, clean packet
    """

    if callsign:
        # If there is a callsign, create a AIS object once. I did not
        # Put the AIS object in the while loop because it constantly would
        # try to reconnect to the APRS server, reinstantiating the object
        # Every time it would run through the loop
        AIS = connect_aprs(callsign)

        while True:

            # Grabbing the packet from aprs.fi servers
            packet = clean_data(AIS)

            # returning the packet as a dictionary
            return packet

            # wait the dwell time before getting another packet
            time.sleep(dwell_time)

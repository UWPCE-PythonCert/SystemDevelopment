#!/usr/bin/env python3

"""
Example code for using logging in a complex system
"""
import sys
import logging
import random
import time
import worker

# The logging configuration:
#  In real life, you might be pulling this from a config file, or ...

# each level of logging gives more information
# uncomment the level you want
# log_level = logging.CRITICAL
# log_level = logging.ERROR
# log_level = logging.WARNING
# log_level = logging.INFO
log_level = logging.DEBUG

# pretty simple format -- time stamp and the message
# this can get fancy:
#  https://docs.python.org/3/library/logging.html#logrecord-attributes
format = '%(asctime)s %(levelname)s - %(module)8s - line:%(lineno)d - %(message)s'

# configure the logger
# basicConfig configures the "root logger" -- usually the one you want.
# this sets it up to write to a file
logging.basicConfig(filename='example.log',
                    filemode='a',  # use 'a' if you want to preserve the old log file
                    format=format,
                    level=log_level)

# and this will make it write to stdout as well
# you would turn this off in production...
if True:  # turn this off with False
    std_handler = logging.StreamHandler(sys.stdout)
    # give this a different formatter:
    formatter = logging.Formatter('%(levelname)9s - %(module)s - %(message)s')
    std_handler.setFormatter(formatter)
    std_handler.setLevel(logging.DEBUG)
    logging.getLogger().addHandler(std_handler)

# Run the "application":
while True:  # keep it running "forever"
    # do something random:
    logging.debug("calling a random worker")
    random.choice(worker.workers)()
    # wait a random length of time :
    time.sleep(random.random())

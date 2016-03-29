"""
A module with lots of random stuff that may happen

This is designed to simulate a complex system --
maybe event driven, etc.

"""

import logging

import random


def work1():
    logging.info("work1 doing a job")


def work2():
    """
    This one randomly logs a warning
    """
    logging.info("work2 doing a job")
    if random.randint(1, 5) == 1:
        logging.warning("something weird happened in work2!")


def work3():
    """
    This one randomly logs an error
    """
    logging.info("work3 doing a job")
    if random.randint(1, 5) == 1:
        logging.error("Error in work3: bad input")


called = [0]


def work4():
    """
    Here something critical can go wrong and crash the system
    """
    logging.info("work4 doing something")
    called[0] += 1
    logging.debug("work4 called {:d} times".format(called[0]))
    if called[0] >= 4:  # don't want it to crash right away :-)
        if random.randint(1, 5) == 1:
            logging.critical("Something went terribly wrong! Aborting!!!")
            raise ValueError("got really, really bad input")

workers = [work1, work2, work3, work4]

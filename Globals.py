import argparse
import errno
import logging
import configparser
import os
import sys

args = None
config = configparser.ConfigParser()
logger = logging.getLogger('root')  # type: logging.Logger
summary = None


def setup_parser():
    global args
    parser = argparse.ArgumentParser(description='Argument parser')
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    # parser.add_argument("-o", "--output_input_dir",
    #                     help="Output/input directory to read features or dump extracted features", type=str,
    #                     default="Data_Dump")
    parser.add_argument("-f", "--config_file", help="The config file to use.", type=str, default='Config.ini')
    args = parser.parse_args()


def setup_logger():
    global logger
    # formatter = logging.Formatter('[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    #                               '%m-%d %H:%M:%S')
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)
    file_handler = logging.FileHandler('VulBench.log')
    stdout_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    logger = logging.getLogger('root')
    if args and args.verbose:
        logger.setLevel(level=logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    logger.addHandler(console_handler)
    logger.addHandler(stdout_handler)
    logger.addHandler(file_handler)


def setup():
    global args
    global config
    global summary
    setup_parser()
    config.read(args.config_file)
    try:
        os.makedirs('results')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    summary = open(config["Summary"]["Path"], 'w')
    setup_logger()


def destroy():
    summary.close()

import argparse
import configparser
import logging
from pkg_resources import resource_filename

from .constants import *


# Entry Point of the Application.
def main():
    # Read Executor Config.
    config = configparser.ConfigParser()
    EXECUTOR_CONFIG_FILE = resource_filename('WopiValidatorExecutor.WopiValidatorExecutor', 'ExecutorConfig.ini')
    config.read(EXECUTOR_CONFIG_FILE)

    defaultWopiDiscoveryServiceUrl = config['DEFAULT'][DEFAULT_WOPIDISCOVERYSERVICEURL]
    defaultTestCategory = config['DEFAULT'][DEFAULT_TESTCATEGORY]

    # Read command line arguments.
    parser = argparse.ArgumentParser(description="WopiValidator Execution Program")
    parser.add_argument('wopisrc', type=str, help="Defines the unencoded WopiSrc Url of .WopiTest file.")
    parser.add_argument('accesstoken', type=str, help="Defines a valid WopiAccessToken.")
    parser.add_argument('-c', type=str, default=defaultTestCategory,
                        help="Defines the target TestCategory, It could either be All, OfficeOnline or OfficeNativeClient and is case-insensitive.")
    parser.add_argument('-s', type=str, default=defaultWopiDiscoveryServiceUrl,
                        help="This represents the WOPI Discovery Service Url for OfficeOnline.")
    parser.add_argument('-v', action="store_const", dest='logLevel', const=logging.DEBUG, default=logging.WARNING,
                        help="Turns on verbose logging")
    args = parser.parse_args()

    # Initialize logging.
    logging.basicConfig(format=EXECUTOR_LOGFORMAT, datefmt=EXECUTOR_DATEFORMAT, filename=EXECUTOR_LOGFILE_NAME,
                        filemode='w', level=args.logLevel)

    # Create Payload.
    payload = {'testcategory': args.c,
               'WOPISrc': args.wopisrc,
               'access_token': args.accesstoken,
               'access_token_ttl': '0'}

    # Execute the WopiValidator.
    from .WopiValidatorExecutor import ExecuteWopiValidator

    ExecuteWopiValidator(args.s, payload)

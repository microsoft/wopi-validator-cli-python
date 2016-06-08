import json
import logging
import requests
import sys
from colorama import init, Fore, Back, Style
from xml.etree import ElementTree

from .constants import *

def GetIndentedJsonDump(inputJson):
    return json.dumps(inputJson, sort_keys=True, indent=4, separators=(',', ': '))

def GetWopiTestEndpoint(wopiDiscoveryServiceUrl):
    logging.info("WOPI Discovery Service Url: " + wopiDiscoveryServiceUrl)
    discoveryServiceResponse = requests.get(wopiDiscoveryServiceUrl)

    try:
        discoveryServiceResponse.raise_for_status()
    except requests.exceptions.HTTPError as exception:
        print(Fore.RED + "Failed to retrieve WOPI Discovery Service XML: Check Logs for more information")
        logging.critical("Failed to retrieve WOPI Discovery Service XML - HTTP ErrorCode: ", exception.Code)
        sys.exit(1)

    try:
        discoveryXml = ElementTree.fromstring(discoveryServiceResponse.content)
        wopiTestEndPointUrl = discoveryXml.find(WOPITESTAPPLICATION_NODE_PATH).attrib[WOPITESTAPPLICATION_URLSRC_ATTRIBUTE]
    except Exception as exception:
         print(Fore.RED + "Failed to parse WOPI Discovery Service XML: Check Logs for more information")
         logging.critical("Failed to parse WOPI Discovery Service XML - Exception Details:", exception)
         sys.exit(1)

    return wopiTestEndPointUrl[:wopiTestEndPointUrl.find('?')]

def ExecuteWopiValidator(wopiDiscoveryServiceUrl, payload):
    # Initialize colorama to allow applying colors to the output text.
    init(autoreset=True)

    wopiTestEndPoint = GetWopiTestEndpoint(wopiDiscoveryServiceUrl)
    logging.info("WopiValidator TestEndpoint Url: " + wopiTestEndPoint)

    print(Fore.CYAN + "..........................WopiValidator Execution Starts....................................\n")

    # Get the TestUrls by calling WopiValidator Endpoint.
    testUrlResponse = requests.get(wopiTestEndPoint, params=payload)

    try:
        testUrlResponse.raise_for_status()
    except requests.exceptions.HTTPError as exception:
        print(Fore.RED + "Execution Failed: Check Logs for more information")
        logging.critical("Failed to retrieve TestUrls - HTTP ErrorCode: ", exception.Code)
        sys.exit(1)

    testurls = testUrlResponse.json()
    logging.info("TestUrls to be Executed : \n" + GetIndentedJsonDump(testurls))

    # Execute tests.
    for testurl in testurls:
        testResultResponse=requests.get(testurl)
        try:
            testResultResponse.raise_for_status()
        except requests.exceptions.HTTPError as exception:
            print(Fore.RED + "Execution Failed: Check Logs for more information")
            logging.critical("HTTP ErrorCode:", exception.Code)
            sys.exit(1)

        # Log the json response for the test being executed.
        testResult = testResultResponse.json();
        logging.info("Result for TestUrl:" + testurl + '\n')
        logging.info(GetIndentedJsonDump(testResult))

        # Print the test result and failure reasons if any.
        testCase = testResult[TEST_NAME]
        errorMsg = testResult[TEST_ERROR_MSG]
        msgColor = Fore.GREEN
        if errorMsg:
            if errorMsg == TEST_ERROR_SKIPPED:
                msgColor = Fore.YELLOW
                print(testCase + msgColor + "...Skipped...\n")
            else:
                msgColor = Fore.RED
                print(testCase + msgColor + "...Failed...\n")
            print(msgColor + errorMsg + '\n')
            requestDetails = testResult[REQUEST_DETAILS]
            for requestDetail in requestDetails:
                validationFailures = requestDetail[REQUEST_VALIDATION_FAILURE]
                failedRequestName = requestDetail[REQUEST_NAME]
                if validationFailures:
                    print(msgColor + "Request Failed: " + failedRequestName)
                    print(msgColor + "*****************FailureReason Starts*********************")
                    for validationFailure in validationFailures:
                        print(msgColor + validationFailure)
                    print(msgColor + "*****************FailureReason Ends***********************\n")
        else:
            print(testCase + msgColor + "...Passed...\n")

    print(Fore.CYAN + "..........................WopiValidator Execution Ends....................................")

# Logging constants
EXECUTOR_DATEFORMAT = '%m/%d/%Y %I:%M:%S %p'
EXECUTOR_LOGFILE_NAME = 'wopivalidatorexecutor.log'
EXECUTOR_LOGFORMAT = '%(asctime)s : %(levelname)s : %(message)s'

# Executor Config Keys
DEFAULT_TESTCATEGORY = 'TestCategory'
DEFAULT_WOPIDISCOVERYSERVICEURL = 'WopiDiscoveryServiceUrl'

# Request JSON elements
REQUEST_DETAILS = 'RequestDetails'
REQUEST_NAME = 'Name'
REQUEST_VALIDATION_FAILURE = 'ValidationFailures'

# TestCase JSON elements
TEST_ERROR_MSG = 'Message'
TEST_ERROR_SKIPPED = 'Prerequisites failed'
TEST_NAME = 'Name'

# XML Parsing constants for WOPI Discovery Service
WOPITESTAPPLICATION_NODE_PATH = './/app/[@name="WopiTest"]/action/[@name="getinfo"]'
WOPITESTAPPLICATION_URLSRC_ATTRIBUTE = 'urlsrc'
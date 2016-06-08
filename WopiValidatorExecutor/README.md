WopiValidatorExecutor
=====================

WopiValidatorExecutor is a command line application which executes the WopiValidator tests to verify the host’s WOPI Implementation.

For more details, please refer the documentation at [Wopi Validator Application](http://wopi.readthedocs.io/projects/officewopi/en/latest/testing/validator.html)

Pre-requisite
-------------

Ensure that you have Python Version >= `2.7` installed.

**Installation Guide**

* [Python Version 2.7](http://docs.python-guide.org/en/latest/starting/installation/)
* [Python Version 3](https://docs.python.org/3/using/windows.html#installing-python)

If you have Python 2 >= `2.7.9` or Python 3 >= `3.4` installed from python.org, you will already have `pip` and `setuptools`, but will need to upgrade to the latest version using the instructions below, (more details at - <https://python-packaging-user-guide.readthedocs.io/en/latest/installing/#install-pip-setuptools-and-wheel>)

**On Linux or OS X**

    pip install -U pip setuptools

**On Windows**

    python -m pip install -U pip setuptools

Installation Steps
------------------

Installation from the source tree :

    $ python setup.py install

* On systems similar to Unix, the installation places a `WopiValidatorExecutor-script` into a centralized `bin` directory, which should be in your `PATH`. 
* On Windows, `WopiValidatorExecutor.exe` will be placed into a centralized `Scripts` directory which should also be in your `PATH`.

Usage
-----

Run the `WopiValidatorExecutor` by passing the `WopiSrc` of the `.wopitest` file and a valid `WOPI AccessToken` enclosed in quotes. :

    $ WopiValidatorExecutor "wopisrc" "accesstoken"

**Optional Arguments**

    -s: If you need to provide a specific Wopi Discovery Service Url, you can pass that Url using 
        this argument.

    -c: If you need to run the WopiValidator in a specific mode, you can pass the intended 
        VALIDATOR_TEST_CATEGORY using this argument. For more details, please refer the documentation 
        at https://wopi.readthedocs.io/en/latest/discovery.html#term-validator-test-category

    -v: Using this argument will turn on verbose logging.

Logs
----

A log file named `wopivalidatorexecutor.log` will be placed in the installation directory.
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from setuptools import setup, find_packages

NAME = "vsts"
VERSION = "0.1.0b0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "msrest>=0.4.5"
]

setup(
    name=NAME,
    version=VERSION,
    description="Python wrapper around the VSTS APIs",
    author="Ted Chambers",
    author_email="vstscli@microsoft.com",
    url="https://github.com/Microsoft/vsts-python-api ",
    keywords=["Microsoft", "VSTS", "Team Services", "SDK", "AzureTfs"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    """
)

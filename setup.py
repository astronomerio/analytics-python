
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Don't import analytics-python module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'analytics'))
from version import VERSION

long_description = '''
*The analytics-python client is created by `Segment <https://segment.com>`_ 
and adapted by `Astronomer <http://www.astronomer.io/>`_.*

It is the simplest way to integrate analytics into your application.
One API allows you to turn on any other analytics service. No more learning
new APIs, repeated code, and wasted development time.

This is the official Python client that wraps the 
`Astronomer API <https://www.astronomer.io/>`_.

Documentation and more details at 
https://github.com/astronomerio/analytics-python
'''

install_requires = [
    "requests>=2.7,<3.0",
    "six>=1.5",
    "python-dateutil>2.1"
]

setup(
    name='astronomer-analytics',
    version=VERSION,
    url='https://github.com/astronomerio/analytics-python',
    author='Astronomer',
    author_email='taylor@astronomer.io',
    maintainer='Astronomer',
    maintainer_email='taylor@astronomer.io',
    test_suite='analytics.test.all',
    packages=['analytics', 'analytics.test'],
    license='MIT License',
    install_requires=install_requires,
    description='The hassle-free way to integrate analytics into any Python application.',
    long_description=long_description,
    keywords='analytics astronomer astronomerio',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
)

#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='cabot-alert-twilio',
      version='1.1.4',
      description='A twilio alert plugin for Cabot by Arachnys',
      author='Arachnys',
      author_email='info@arachnys.org',
      url='http://cabotapp.com',
      packages=find_packages(),
      download_url= 'https://github.com/bonniejools/cabot-alert-twilio/tarball/1.1.4',
      install_requires=[
            'phonenumbers==7.2.2',
    ],
     )

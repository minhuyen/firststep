from setuptools import setup

import os

# Put here required packages
packages = ['Django<=1.6.5',]

if 'REDISCLOUD_URL' in os.environ and 'REDISCLOUD_PORT' in os.environ and 'REDISCLOUD_PASSWORD' in os.environ:
     packages.append('django-redis-cache')
     packages.append('hiredis')

setup(name='firststep',
      version='1.0',
      description='OpenShift App',
      author='Uyen Do',
      author_email='minhuyendo@gmail.com',
      url='https://pypi.python.org/pypi',
      install_requires=packages,
)


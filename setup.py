# -*- coding: utf-8 -*-
from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='remote_configurator',
      version='0.1',
      description='Send/receive remote configurations through TCP',
      long_description=readme(),
      classifiers=[
        'Programming Language :: Python :: 2.7',
        'Topic :: Networking :: TCP',
      ],
      keywords='remote configuration RadioGIS TCP',
      url='http://github.com/98789/remote_configurator',
      author='Jesús Muñoz',
      author_email='jmunoz@radioGIS.uis.edu.co',
      packages=['remote_configurator'],
      include_package_data=True,
      zip_safe=False)

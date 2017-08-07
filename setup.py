import re
from os.path import join, dirname
from setuptools import setup, find_packages

# reading package version (same way the sqlalchemy does)
with open(join(dirname(__file__), 'pytb', '__init__.py')) as v_file:
    package_version = 'v0.1.1'

dependencies = [
    'python-telegram-bot',
    'ujson',
    'requests',
    'webtest',
    'nose'
]

setup(
    name="pytb",
    version=package_version,
    author="Perfect",
    author_email="mahdi_1373@yahoo.com",
    install_requires=dependencies,
    packages=find_packages(),
    test_suite="pytb.tests",
    message_extractors={'pytb': [
        ('**.py', 'python', None),
    ]},
)

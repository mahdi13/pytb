from setuptools import setup, find_packages

package_version = 'v0.1.2'

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

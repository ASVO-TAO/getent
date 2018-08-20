from setuptools import setup, find_packages

setup(
    name         = 'getent',
    version      = '0.2',
    author       = 'Wijnand Modderman-Lenstra',
    author_email = 'maze@pyth0n.org',
    description  = 'Python interface to the POSIX getent family of commands',
    long_description = open('README.rst', encoding="utf-8").read(),
    license      = 'MIT',
    keywords     = 'getent group passwd shadow network alias host',
    packages     = ['getent'],
)


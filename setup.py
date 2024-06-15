from setuptools import setup, find_packages

setup(
    name="termy",
    version="0.0",
    packages=find_packages(),
    install_requires=[
        'curses',
        'windows-curses',
        'pyfiglet',
        'termcolor',
        're',
        'os'
    ]

)
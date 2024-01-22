# setup.py
from setuptools import setup

setup(
    name='topsis-vineet-102103465',
    version='0.1',
    packages=['topsis'],
    install_requires=['numpy'],
    entry_points={
        'console_scripts': [
            'topsis-cli = topsis.topsis:main',
        ],
    },
)


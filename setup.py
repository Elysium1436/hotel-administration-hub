from setuptools import setup

setup(
    name='mongtest',
    version='0.1.0',
    pymodules=['mongtest'],
    install_requires=[
        'Click',
        'mongoengine',
        'tabulate'
    ],
    entry_points={
        'console_scripts': [
            'mongtest = api.main:cli',
        ]
    }
)

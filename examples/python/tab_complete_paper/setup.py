from setuptools import setup

setup(
    name='paper-url',
    install_requires=[
        'requests',
        'click==8.*',
    ],
    entry_points={
        'console_scripts': [
            'paper-url = cli:cli',
        ],
    },
)

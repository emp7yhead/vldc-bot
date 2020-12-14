# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ''

setup(
    long_description=readme,
    name='vldc-bot',
    version='0.4.11',
    description='VLDC nyan bot ^_^',
    python_requires='==3.*,>=3.8.0',
    author='@egregors',
    maintainer='@cpro29a',
    packages=['bot', 'bot.db', 'bot.skills', 'bot.tests', 'bot.utils'],
    package_dir={"": "."},
    package_data={},
    install_requires=[
        'google-cloud-automl==0.10.0', 'google-cloud-speech==2.0.0',
        'google-cloud-translate==2.0.0', 'pillow==8.*,>=8.0.1',
        'pymongo==3.11.0', 'python-telegram-bot==13.0', 'sentry-sdk==0.19'
    ],
    extras_require={
        "dev": [
            "flake8==3.8.4", "mypy==0.790", "ptvsd==4.3.2", "pytest==5.1.2"
        ]
    },
)

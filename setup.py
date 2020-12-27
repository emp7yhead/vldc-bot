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
    version='0.5.3',
    description='VLDC nyan bot ^_^',
    python_requires='==3.*,>=3.9.0',
    author='@egregors',
    maintainer='@cpro29a',
    packages=['bot', 'bot.db', 'bot.skills', 'bot.tests', 'bot.utils'],
    package_dir={"": "."},
    package_data={},
    install_requires=[
        'google-cloud-automl==0.10.0', 'google-cloud-speech==2.0.0',
        'google-cloud-translate==2.0.0', 'pillow==8.*,>=8.0.0',
        'pymongo==3.*,>=3.11.0', 'python-telegram-bot==13.0',
        'sentry-sdk==0.*,>=0.19.0', 'toml==0.10.2'
    ],
    extras_require={
        "dev": [
            "flake8==3.*,>=3.0.0", "mypy==0.790", "ptvsd==4.3.2",
            "pylint==2.*,>=2.0.0", "pytest==5.1.2"
        ]
    },
)

from setuptools import setup, find_packages
from os import path

this_directory  = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='UCASicsAlt',
    version='0.0.5',
    packages=find_packages(),
    install_requires=['Click',
                      ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': ['ucasicsalt=UCASicsAlt.add_notification:cli']
    },
)

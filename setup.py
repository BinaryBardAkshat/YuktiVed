
from setuptools import setup, find_packages

setup(
    name='yuktived',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
    ],
    author='Akshat Shukla',
    author_email='akshatshukla317@gmail.com',
    description='A Python library for data analysis and machine learning',
    license='MIT',
    
)


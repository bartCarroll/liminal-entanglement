# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('../README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='liminal-entanglement',
    version='1.0.0',
    description='Interactive Art Piece',
    long_description=readme,
    author='Bart Carroll',
    author_email='xironoarx@gmail.com',
    url='https://github.com/bacarroll/liminal-entanglement',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=['serial', 'pillow', 'pyserial', 'playsound', 'keyboard', 'pygame']
)

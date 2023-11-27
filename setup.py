from setuptools import setup, find_packages
import os

setup(
    name='MacNet',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='The MacNet Python Package Manager.',
)

open(f"{os.getenv('HOME')}/.zshrc", "a").write("alias macnet='python3 -m macnet'")
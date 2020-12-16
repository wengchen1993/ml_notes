from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name="ML Notes",
    version="0.1",
    description="Collection of personal ML notes.",
    author="Weng Hoe Chen",
    packages=find_packages()
)

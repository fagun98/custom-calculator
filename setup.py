from setuptools import setup, find_packages

setup(
    name="custom_calculator",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "mathlib",  # No need to install as math is built-in, this is for reference.
    ],
    description="A simple calculator module with basic and advanced mathematical functions.",
    author="Fagun Raithatha",
    url="https://github.com/fagun98/custom-calculator.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)

import setuptools
from waycheck.version import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="waycheck",
    version=__version__,
    author="AbleInc - Jaylen Douglas",
    author_email="douglas.jaylen@gmail.com",
    description="A lightweight Python type checker. Designed with the developer in mind.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ableinc/waycheck",
    keywords=['waycheck', 'typechecker', 'type', 'check', 'assertion', 'assertion check', 'python types',
    'ableinc', 'python type check', 'python type checker', 'python decorator', 'decorator', 'decorator class',
    'type check decorator'],
    packages=['waycheck'],
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
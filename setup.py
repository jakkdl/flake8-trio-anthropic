#!/usr/bin/env python3
"""setup, registering for pip and using setuptools entry point to register with flake8"""
import setuptools

NAME = "flake8_trio_anthropic"

requires = [
        "flake8 >= 3.9.0",
        ]

setuptools.setup(
    name=NAME,
    version='0.1.0',
    author="John Litborn",
    author_email="john.litborn+FTA@pm.me",
    py_modules=[NAME],
    url=f"https://github.com/jakkdl/{NAME}",
    license="MIT",
    description="A flake8 plugin that checks for bad Trio code",
    zip_safe=False,
    install_requires=requires,
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Flake8",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    #long_description=(
    #    local_file("README.md").open().read()
    #    + "\n\n"
    #    + local_file("CHANGELOG.md").open().read()
    #),
    #long_description_content_type="text/markdown",
    entry_points={
        "flake8.extension": [
            f"TRIO0 = {NAME}:Plugin"
            ],
    },
)

# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name="dot_kernel",
    version="0.1.5",
    url="https://github.com/laixintao/jupyter-dot-kernel",
    author="laixintao",
    author_email="laixintao1995@163.com",
    description="Writing dot language and render in jupyter.",
    packages=find_packages(),
    install_requires=["graphviz", "jupyter"],
    scripts=['bin/install-dot-kernel']
)

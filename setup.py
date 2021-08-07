from setuptools import setup

setup(name="CloudTrim",
version="0.0.1",
description="for trimming online videos",
long_description="this package is devloped to be meant to use in google colab for trimming and downloading videos",
author="Alvin Saini",
license='MIT',
author_email="codewithalvin@gmail.com",
packages=["CloudTrim"],
install_requires=["moviepy","googledrivedownloader"]
)

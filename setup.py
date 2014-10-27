#! /usr/bin/python
from setuptools import setup
import os.path

setup(name='passencode',
      version='1.0.0',
      description='Passencode',
      author='Nicolas Vanhoren',
      author_email='nicolas.vanhoren@unknown.com',
      url='http://pygreen.neoname.eu',
      py_modules = ['pygreen'],
      packages=[],
      scripts=["pygreen"],
      long_description="A micro web framework/static web site generator.",
      keywords="",
      license="MIT",
      classifiers=[
          ],
      install_requires=[
        "flask >= 0.10.1",
        "mako >= 0.8.0",
        "argparse",
        "markdown",
        ],
     )


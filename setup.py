
import os, sys

try:
    from setuptools import setup
except:
    from distutils.core import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def read_requirements(fname):
    f = open(os.path.join(os.path.dirname(__file__), fname))
    return filter(lambda f: f != '', map(lambda f: f.strip(), f.readlines()))

setup(
    zip_safe = False,
    name = "django-bootstrap-static-files",
    version = "3.0.0-wip",
    author = "Charles Hathaway",
    author_email = "chathaway@logrit.com",
    description = "This package provides the Bootstrap files in a simple Django app.",
    keywords = "django bootstrap static files",
    packages=['bootstrap_static_files', 'bootstrap_static_files.templatetags'],
    long_description=read('README.md'),
    install_requires = read_requirements('libraries.txt'),
    test_suite = "dummy",
)

import os,sys
from setuptools import setup
from subprocess import call

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "photo_storage_cli",
    version = "0.0.1",
    author = "Chris Cohoat",
    author_email = "chris.cohoat@gmail.com",
    description = ("A simple (emphasis on simple) CLI for a photo storage system."),
    license = "BSD",
    url = "http://photo-storage.herokuapp.com",
    packages=['photos_cli'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=['pycurl','requests'],
)

bindir = '/usr/local/bin'

file_to_copy = 'photos' 

path_to_cli = os.path.join(os.path.dirname(os.path.abspath(__file__)),'photos_cli/%s' % file_to_copy)
command = "cp %s %s" % (path_to_cli,bindir)
os.system(command)

#Make file executable
new_path = os.path.join(bindir,file_to_copy)
os.system('chmod +x %s' % new_path)

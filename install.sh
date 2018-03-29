#!/bin/bash -e

# install homebrew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# install python
brew install python

# install pip
sudo easy_install pip

# install python packages
pip install pyzipcode
# geopy docs: http://geopy.readthedocs.io/en/latest/
pip install geopy

#! /usr/bin/env bash
#
# Sets up the virtual Python environment.
#
yum install -y gettext
python3 -m venv .venv
source .venv/bin/activate
pushd build
pip install -r ./requirements.txt

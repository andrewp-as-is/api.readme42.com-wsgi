#!/bin/sh

cd /Users/russianidiot/git/andrewp-as-is/django-configurations-ec2.py

export README42_TOKEN=55acd5f3c12cfcc121c02b6b14ace9a5
export README42_TEMPLATE=andrewp-as-is/python-github-readme
export README42_NAME="$(IFS=.;set ${PWD##*/};echo $1)"

readme42 . > "${BASH_SOURCE[0]%/*}"/README.md

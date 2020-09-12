#!/bin/bash

sudo apt-get update

sudo apt-get install git  python3-pip apache2 libapache2-mod-wsgi-py3

sudo pip3 install virtualenv

virtualenv myprojectenv

git clone https://github.com/edwinhazel/Hackaton.git

mkdir ./ayudanteenv

virtualenv ./ayudanteenv

echo "source ./ayudanteenv/bin/activate"


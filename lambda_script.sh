#!/bin/bash


mkdir -p python

pip install -r requirements.txt -t python/

zip -r "layer.zip" python

zip -r "$src.zip" src

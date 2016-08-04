#!/usr/bin/env bash

(cd base; cython *.pyx)

pip install --upgrade --user -e .

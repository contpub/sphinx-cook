#!/bin/bash

# make clean
make epub
make pdflatex

cp -f _build/latex/*.pdf free/
cp -f _build/epub/*.epub free/

make clean

open free/*.pdf


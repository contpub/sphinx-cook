#!/bin/bash

# make clean
make epub
make latexpdf

cp -f _build/latex/*.pdf free/
cp -f _build/epub/*.epub free/
cp -f _build/mobi/*.mobi free/

make clean

open free/*.pdf


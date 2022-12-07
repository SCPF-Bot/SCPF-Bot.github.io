#!/bin/bash

rm -rf pages
mkdir -p pages

cat origin/origin.md temp/patches.md > pages/patches.md

rm -rf temp
mkdir -p temp

cat > temp/temp.bin

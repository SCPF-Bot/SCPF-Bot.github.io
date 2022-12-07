#!/bin/bash

mkdir -p temp

wget https://raw.githubusercontent.com/revanced/revanced-patches/main/CHANGELOG.md -o temp/patches.md

rm -rf pages

mkdir -p pages

cat origin/origin.md temp/patches.md > pages/patches.md

rm -rf temp

#!/bin/bash

mkdir -p temp

curl -o temp/patches.md https://raw.githubusercontent.com/revanced/revanced-patches/main/CHANGELOG.md

rm -rf pages

mkdir -p pages

cat origin/origin.md temp/patches.md > pages/patches.md

rm -rf temp

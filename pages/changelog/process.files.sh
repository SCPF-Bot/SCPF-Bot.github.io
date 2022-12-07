#!/bin/bash

rm -rf changelogs
mkdir -p changelogs

cat origin/origin.md temp/patches.md > changelogs/patches.md

rm -rf temp

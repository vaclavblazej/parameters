#!/usr/bin/env bash

cd "$(dirname "$0")" || exit
target_folder="../content/html"
./draw.py
cp ./build/*.md "$target_folder/"
cp ./build/*.pdf "$target_folder/"

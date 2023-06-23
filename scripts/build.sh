#!/usr/bin/env bash

cd "$(dirname "$0")" || exit
target_folder="../content/html"
./draw.py
cp "./build/page.md" "$target_folder/index.md"
cp "./build/parameters.pdf" "$target_folder/parameters.pdf"

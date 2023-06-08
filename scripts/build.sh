#!/usr/bin/env bash

cd "$(dirname "$0")" || exit
target_folder="../content"
./draw.py
cp "./page.md" "$target_folder/index.md"
cp "./parameters.pdf" "$target_folder/parameters.pdf"

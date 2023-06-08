#!/usr/bin/env bash

target_folder="$HOME/Dropbox/Projects/vasek_pages/content/material/science/cpx/parameters"
./draw.py
cp "./page.md" "$target_folder/index.md"
cp "./parameters.pdf" "$target_folder/parameters.pdf"

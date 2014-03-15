#!/bin/bash

# Install pandoc if unavailable
sudo apt-get install pandoc

# Remove existing final.md
rm final.md

# Compile it into one
for f in README.md getting_it.md code_devel.md using_it.md scope.md faqs.md 
do
	cat $f >> final.md
done
pandoc final.md -o one.html

echo "Check one.html";

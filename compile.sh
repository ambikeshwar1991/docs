#!/bin/bash

# Install pandoc if unavailable
sudo apt-get install pandoc

# Compile it into one
for f in README.md getting_it.md code_devel.md using_it.md scope.md faqs.md 
do
	cat $f >> final.md
done
pandoc final.md -o one_page_doc.html

# Remove final.md
rm final.md

if [ $? -eq 0 ]; then
echo "Check one_page_doc.html";
fi

#!/bin/sh

# simple script to build and push to gh-pages
# designed to be run from master

# make the docs
make html

# copy to other repo (on the gh-pages branch)
cp -R build/html/ ../../SystemDevelopment.gh-pages

# copy html_slides also:
cp -R html_slides ../../SystemDevelopment.gh-pages

cd ../../SystemDevelopment.gh-pages
git add * # in case there are new files added
git commit -a -m "updating presentation materials"
git push


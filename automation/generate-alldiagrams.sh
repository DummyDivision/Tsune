#!/bin/bash

#delete old outputs
rm -rf ./output

#create output directory
mkdir output

#get all .py files related to views, make them readable for pyreverse (module form)
views=`find /vagrant/ -name "*form*.py"  -o -name "*view*.py" -printf "%p "`
views=$(sed 's|.py||g' <<< $views)
views=$(sed 's|/vagrant/||g' <<< $views)
views=$(sed 's|/|.|g' <<< $views)

#get all .py files related to modules, make them readable for pyreverse (module form)
models=`find /vagrant/ -name "*model*.py" -printf "%p "`
models=$(sed 's|.py||g' <<< $models)
models=$(sed 's|/vagrant/||g' <<< $models)
models=$(sed 's|/|.|g' <<< $models)

#get all template html files
templates=`find /vagrant/ -name "*.html" -not -path /vagrant/docs -printf "%p "`

#execute script to generate .dot file based on templates hierarchy
python generate-templatedia.py $templates

#convert templates dot file to png
dot -Tpng templates.dot > output/templates_dia.png
rm templates.dot

#use pyreverse for views and models
cd ..
pyreverse -o png -a 2 -p tsune_views $views
pyreverse -o png -a 2 -p tsune_models $models

#delete unneseccary files, move both class diagrams
rm packages_tsune_models.png
rm packages_tsune_views.png
mv classes_tsune_models.png automation/output/models_dia.png
mv classes_tsune_views.png automation/output/views_dia.png
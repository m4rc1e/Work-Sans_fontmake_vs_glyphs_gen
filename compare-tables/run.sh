#!/bin/bash

# Generate fonts with fontmake
cd ./fontmake_gen/

# Delete old ttx files and fontmake gens
for file in *.ttx; do
    rm "$file"
done
rm -r instance_ttf/ instance_ufo/ master_ufo


fontmake -g '../../Work-Sans/sources/Work Sans.glyphs' -o ttf -i --production-name

# Convert fontmake ttf's into ttx
for file in ./instance_ttf/*.ttf; do
        ttx -d . "$file"
done

cd ../glyphs_gen/
# Delete old ttx files 
for file in *.ttx; do
    rm "$file"
done

# Convert glyphs generated ttf into ttx
# These fonts had to be generated manually in Glyphs 2.0, due to lack of headless version of app
for file in ./instance_ttf/*.ttf; do
        ttx -d . "$file"
done
#!/bin/bash

# Generate fonts with fontmake
cd ./fontmake_gen/

# Remove prevously generated sources
rm -r instance_ttf/ instance_ufo/ master_ufo


fontmake -g '../smart-components.glyphs' -o ttf -i --production-name
cd ..

# Run unittests to check if fontmake has decomposed smart comps
python test.py

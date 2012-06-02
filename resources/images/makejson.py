#!/usr/bin/env python


import os
import json


for arttype in ('newspapers', 'photographs', 'pictures'):
    l = []
    for filename in os.listdir(arttype):
        l.append({'image': os.path.join('resources/images/' + arttype + '/',
            filename)})
    with open(arttype + '.json', 'wb') as fout:
        json.dump(l, fout, indent=4)
        fout.write('\n')

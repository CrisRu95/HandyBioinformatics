#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script que transforma los fichero de seqmask en un fasta de referencia
Pegando tal cual los trozos de secuencia
NO tiene en cuenta el tamanyo de intron (y es que me da igual)
"""

import re


file = input("Inserte la ruta y nombre del fichero :")

with open(file, 'r') as seqmaskfile: 
    with open('ref.fa', 'w') as reffile: 
        for line in seqmaskfile.readlines():
            if re.match('^[actgn]+$', line, flags = re.I):
                line = line.replace('\n', '')
                reffile.write(line)
                
                

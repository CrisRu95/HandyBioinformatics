#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 13:20:04 2019

@author: Cristina

A este programa se le dará un directorio de salida de exonprocess con todos los
ficheros de primer 3 ---> Y sacará un fichero de todos los fastq conjuntos de 
primers y de slices
"""

import os

#Generamos la lista de carpetas que tienen los fqs
everything = os.listdir()
dirs = []

for file_or_dir in everything: 
    if '_Exon' in file_or_dir and os.path.isdir(file_or_dir):
        dirs.append(file_or_dir)


#Generamos un mega fq para los slices
with open('allslices.fq', 'a+') as slices: 
    for directory in dirs: 
        to_open = directory + '/' + 'slices2.fq'
        with open(to_open, 'r') as smallslices: 
            string = smallslices.read()
            slices.write(string)


#Generamos un mega fq para los primers
with open('allprimers.fq', 'a+') as primers: 
    for directory in dirs: 
        to_open = directory + '/' + 'primers2.fq'
        with open(to_open, 'r') as smallprimers: 
            string = smallprimers.read()
            primers.write(string)
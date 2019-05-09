#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:35:05 2019

@author: ugdg
"""

ffile = input("Introduce el nombre del fichero con la secuencia de ensembl en feo: ")

newfile = input("Introduce el nombre del NUEVO fichero: ")
cabecera = input("Introduce la cabecera del fasta: ")

with open(ffile, 'r') as file: 
    with open(newfile, 'w') as nfile: 
        cabecera = cabecera + '\n'
        nfile.write(cabecera)
        string = ''
        
        for line in file.readlines():
            nline = line.replace('\n', '') #quitamos newlines
            nline = nline.replace(' ', '') #quitamos espacios
            nline = nline.replace('.', '') #quitamos puntos (intrones largos)
            string = string + nline #concatenamos
        
        nfile.write(string) #lo escribimos al final
            
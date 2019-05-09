#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:44:16 2019

@author: Cristina
"""
import re

seqmaskfile = input("Introduce el nombre del fichero seqmask a transformar: ")

fqfile = input("Nombre del fichero fq a generar: ")

with open(seqmaskfile, 'r') as sfile: 
    with open(fqfile, 'w') as ffile: 
        for line in sfile.readlines(): 
            
            if '>' in line: 
                line = line.replace('>', '@') #nuevo identificador
                ffile.write(line) #escribimos el identificador
            
            elif re.match('[ACTGN]+$', line.upper()): 
                #ACTG.. \n + \n ACTG...
                string = line + '+' + '\n' + line 
                ffile.write(string)
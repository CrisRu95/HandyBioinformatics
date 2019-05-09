#!/bin/bash

#Pedimos los datos iniciales al usuario:
read -p "Inserte el nombre del fichero con la secuencia de referencia: " file_ref
read -p "Inserte el nombre del fq: " file_fq

bwa index $file_ref

bwa mem $file_ref $file_fq > sfile.sam
samtools view -bS sfile.sam > sfile.bam
samtools sort sfile.bam -o sfile.sorted.bam
samtools index sfile.sorted.bam


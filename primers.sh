#!/bin/bash

#Pedimos los datos iniciales al usuario:
read -p "Inserte el nombre del fichero con la secuencia de referencia: " file_ref
read -p "Inserte el nombre del fq: " file_fq

bwa index $file_ref

bwa aln $file_ref $file_fq > paln_sa.sai

bwa samse $file_ref paln_sa.sai $file_fq > paln.sam

samtools view -bS paln.sam > pfile.bam
samtools sort pfile.bam -o pfile.sorted.bam
samtools index pfile.sorted.bam


#!/bin/bash
#$ -S /bin/bash
#$ -cwd
module load python/2.7
echo $SECONDS
python2.7 mmu-miR-125a-5p-5utr.py
echo $SECONDS
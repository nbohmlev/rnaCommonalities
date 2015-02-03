#!/bin/bash
#$ -S /bin/bash
#$ -cwd
echo $SECONDS
module load python/2.7
python2.7 ./jobs/mmu-miR-9-5p.py
echo $SECONDS
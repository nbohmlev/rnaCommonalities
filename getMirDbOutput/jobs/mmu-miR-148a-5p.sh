#!/bin/bash
#$ -S /bin/bash
#$ -cwd
echo $SECONDS
module load python/2.7
python2.7 ./jobs/mmu-miR-148a-5p.py
echo $SECONDS
from rnaMotifs.getMirDbOutputSrc import mirDbBotWrapper as MB
import ipdb
import subprocess

if __name__ == "__main__":
    
    mirName=['mmu-miR-125a-5p',
             'mmu-miR-125a-3p',
             'mmu-miR-101a-5p',
             'mmu-miR-101a-3p',
             'mmu-miR-101b-5p',
             'mmu-miR-101b-3p',
             'mmu-miR-129-5p',#
             'mmu-miR-221-5p',
             'mmu-miR-221-3p',
             'mmu-miR-9-5p',
             'mmu-miR-9-3p',
             'mmu-miR-124-5p',
             'mmu-miR-124-3p',
             'mmu-miR-125b-5p',
             'mmu-miR-125b-1-3p',#
             'mmu-miR-125b-2-3p',#
             'mmu-miR-132-5p',
             'mmu-miR-132-3p',
             'mmu-miR-376a-5p',
             'mmu-miR-376a-3p',
             'mmu-miR-34b-5p',
             'mmu-miR-34b-3p',
             'mmu-miR-324-5p',
             'mmu-miR-324-3p',
             'mmu-miR-301a-5p',
             'mmu-miR-301a-3p',
             'mmu-miR-101a-5p',
             'mmu-miR-101a-3p',
             'mmu-miR-148a-5p',
             'mmu-miR-148a-3p',
             'mmu-miR-380-5p',
             'mmu-miR-380-3p',
             'mmu-miR-340-5p',
             'mmu-miR-340-3p',
             'mmu-miR-30e-5p',
             'mmu-miR-30e-3p',
             ]
    
    dirPath = "./jobs"
    #ipdb.set_trace()
    for item in mirName:
        with open(dirPath + "/allJobs.sh", 'a') as fout:
            fout.writelines('qsub %s/%s.sh\n' %(dirPath, item))

        
        with open('%s/%s.sh' % (dirPath, item), 'w') as fout:
            ls = "#!/bin/bash\n#$ -S /bin/bash\n#$ -cwd\necho $SECONDS\nmodule load python/2.7\npython2.7 %s/%s.py\necho $SECONDS" %(dirPath, item)
            fout.writelines(ls)
        
        with open('%s/%s.py' % (dirPath, item), 'w') as fout:
            ls = "#!/usr/bin/env python\nfrom rnaMotifs.getMirDbOutputSrc import mirDbBotWrapper as MB\nif __name__=='__main__':\n\tmirName = '%s'\n\tMB.mirDbBotWrapper(mirName)\n"%(item)
            fout.writelines(ls)
    
            
    subprocess.Popen('chmod u+x %s/*.sh' % (dirPath), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)    

    p = subprocess.Popen('%s/allJobs.sh' %(dirPath), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    print (p.stdout.read())

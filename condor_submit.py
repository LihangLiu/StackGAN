import os
import glob

version = 'stack_I'

### run file
Executable_file = 'run_%s.sh' % (version)
with open(Executable_file, 'w') as f:
	f.write("""#!/bin/bash
source activate tensorflow
export PYTHONPATH=/scratch/cluster/leonliu/repos/StackGAN:$PYTHONPATH
python stageI/run_exp.py --cfg stageI/cfg/birds.yml
""")
print(Executable_file, 'generated')
os.system('chmod 755 %s'%(Executable_file))


### condor submit file
submit_config_file = """+Group="GRAD"
+Project="AI_ROBOTICS"
+ProjectDescription="nlp Project"
+GPUJob=true
Requirements=(TARGET.GPUSlot && Eldar == True) 
Rank=memory
Environment=PATH=/scratch/cluster/leonliu/anaconda3/bin:/lusr/opt/condor/bin/:/lusr/opt/condor/bin/:/opt/cuda-8.0/bin:$PATH
Environment=PYTHONPATH=/u/leonliu/.local/lib/python2.7/site-packages:$PYTHONPATH
Environment=LD_LIBRARY_PATH=/u/leonliu/repos/cuDNN:/u/leonliu/repos/cuDNN/lib64:/opt/cuda-8.0/lib:/opt/cuda-8.0/lib64:$LD_LIBRARY_PATH

Universe=vanilla
Getenv=True

Log=outputs/log/{0}log.$(Cluster).$(Process) 
Output=outputs/log/{0}out.$(Cluster).$(Process) 
Error=outputs/log/{0}err.$(Cluster).$(Process)
Executable={1}

Queue 1
""".format(version,Executable_file)


with open('condor_submit', 'w') as f:
	f.write(submit_config_file)
print('condor_submit generated')

os.system("condor_submit condor_submit")








#!/bin/bash
source activate tensorflow
export PYTHONPATH=/scratch/cluster/leonliu/repos/StackGAN:$PYTHONPATH
python -m stageInfo.run_exp --cfg stageInfo/cfg/birds.yml

#!/bin/sh

if [ "$1" = "clean" ]; then
    for file in `ls RelVal*.txt`
      do
      dataset=${file%.*}
      echo Removing $dataset
      rm -r $dataset
    done
    rm submitall.sh
    exit 0
fi

pwd=`pwd`

echo $pwd

# create submit-all script
touch submitall.sh
chmod u+x submitall.sh

for file in `ls RelVal*.txt`
  do
  
  dataset=${file%.*}
  echo Making config for $dataset
  
# create test area
  mkdir $dataset
  
# copy job config file and delete final line }
  sed '$d' $CMSSW_BASE/src/L1Trigger/Configuration/test/l1validation.cfg > $dataset/l1validation.cfg
  
# cat datasets to configs and add final }
  cat $dataset.txt >> $dataset/l1validation.cfg
  cat >> $dataset/l1validation.cfg <<-EOF
}
EOF
  
# create batch script
  cat >> $dataset/batch.sh <<EOF
#!/bin/bash
cd $pwd/$dataset
`scramv1 runtime -sh`
export STAGE_SVCCLASS=default
cmsRun l1validation.cfg > log
EOF
  
# add a line to batch submit
  cat >> submitall.sh<<EOF
bsub -q1nh $dataset/batch.sh $dataset
EOF
  
done

exit 0


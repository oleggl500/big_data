# How to run map-reduce jobs on docker hadoop streaming

## Task
Data taken from [here](http://sdm.lbl.gov/fastbit/data/star2002-full.csv.gz)

Data Columns:
1. antiNucleus INT
* eventFile UINT
* eventNumber INT
* eventTime DOUBLE
* histFile UINT
* multiplicity INT
* NaboveLb INT
* NbelowLb INT
* NLb  INT
* primaryTracks INT
* prodTime DOUBLE
* Pt  FLOAT
* runNumber INT
* vertexX  FLOAT
* vertexY  FLOAT
* vertexZ  FLOAT

First task is to take data which prodTime values lies between 5% and 95% percentiles. Second task is to print number of unique values 
of eventFile and averange of Pt for each unique antiNucleus. To test map-reduce jobs in terminal:
```shell
cat star2002-sample.csv | python map1.py | sort -k1,1 | python reduce1.py | sort -k1,1 | python reduce2.py | sort -k1,1 | python reduce_last.py > output.txt
```

## Testing in hadoop-docker
1. Run [docker](https://docs.docker.com/compose/install/):
sudo docker run -it sequenceiq/hadoop-docker:2.7.1 /etc/bootstrap.sh -bash

2. In local terminal:
    ```shell
   sudo docker ps
   ```
   copy name of docker in my case wonderful_mcnulty. After that copy data and all mapers and reducers to docker
   ```shell
   sudo docker cp ./star2002-sample.csv wonderful_mcnulty:sample.csv
   sudo docker cp ./map1.py wonderful_mcnulty:map1.py
   sudo docker cp ./reduce1.py wonderful_mcnulty:reduce1.py
   sudo docker cp ./reduce2.py wonderful_mcnulty:reduce2.py
   sudo docker cp ./reduce3.py wonderful_mcnulty:reduce3.py
   ```
   
3. In docker:

    ```shell
    cd $HADOOP_PREFIX
    bin/hdfs dfs -mkdir sample
    bin/hdfs dfs -put /sample.csv ./sample
    ```
    ```shell
    bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
        -input sample/ \
        -output ./output \
        -mapper map1.py \
        -reducer reduce1.py \
        -file /map1.py \
        -file /reduce1.py
    ```
    ```shell
    bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
        -input ./output \
        -output ./output1 \
        -mapper cat \
        -reducer reduce2.py \
        -file /reduce2.py
    ```
    ```shell
    bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
        -input ./output1 \
        -output ./output2 \
        -mapper cat \
        -reducer reduce3.py \
        -file /reduce3.py
    ```
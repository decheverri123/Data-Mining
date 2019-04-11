Implementation and evaluation of a MapReduce algorithm for mining (approximately) the frequent itemsets from a dataset. 

Used the SON Apriori algorithm with Hadoop to mine the blocks of transactions in the first Map.




How to run: 

hadoop jar mr.jar MRMiner MINSUPP CORR TRANS_PER_BLOCK PATH_TO_INPUT PATH_TO_FIRST_OUT PATH_TO_FINAL_OUT

..* MINSUPP, an integer, is the minimum support threshold;
..* CORR, an integer, is the “correction” to the minimum support threshold: the first Map function will mine the set of transactions it receives with a minimum support threshold of MINSUPP-CORR.
..* TRANS PER BLOCK, an integer, is the number oftransactions per “block” ofthe dataset, which are simultaneously given in input to the first Map function (see below, where implementation details are discussed).
..* PATH TO INPUT is the path to the HDFS input directory containing the input dataset (format described below);
..* PATH TO FIRST OUT is the path to the HDFS output directory for the first round; • PATH TO FINAL OUT is the path to the HDFS final output directory (format described below).

## Introduction

This is an implementation of the algorithms from the [TRIEST paper](https://arxiv.org/abs/1602.07424) that are used for counting localTriangles and totalTriangles triangles in fully dynamic streams with fixed memory size. 

This repository contains the algorithm 1 (TRIEST-BASE) and 2 (TRIEST-IMPR). 

The implementation results are shown on the [arXiv astro-ph dataset](http://konect.uni-koblenz.de/networks/ca-AstroPh).  

## Running The Solution
Implementation is done using Python 3.

To run the code:  `python run.py`

To run TRIEST-BASE algorithm, set `mode=1` in run.py. For TRIEST-IMPR algorithm , set `mode=2` in run.py. 

## Dataset Description
The [dataset](http://konect.uni-koblenz.de/networks/ca-AstroPh) represents the collaboration graph of authors of scientific papers from the arXiv's Astrophysics (astro-ph) section. 

The graph is undirected and unweighted and an edge between two authors represents a common publication. 
The dataset contains 18,771 vertices (authors) and 198,050 Edges (collaborations).

## Implementation
TRIEST-BASE and TRIEST-IMPR algorithms are implemented.

Both of them are based on [reservoir sampling](https://dl.acm.org/citation.cfm?id=3165), so that was implemented.

Experiments with different sample sizes to see the performance of these algorithms and results are shown in the next section.

## Results

**For different sample sizes:**

Figure 1 and 2 show that TRIEST-BASE shows more variance than TRIEST-IMPR on changing the sample sizes. 
Both of the algorithms show 7000 as a good sample size.

![Figure1](/imgs/T1.png)
![Figure2](/imgs/T2.png)

**For same sample size and multiple iterations:**

Figure 3 and 4 show that TRIEST-BASE shows more variance when we keep the sample size fixed. 
In this case, the sample size was 7000 for both TRIEST-BASE and TRIEST-IMPR.

![Figure3](/imgs/T3.png)
![Figure4](/imgs/T4.png)

#!/bin/bash

java -cp .\hanlp-portable-1.7.4.jar com.hankcs.hanlp.mining.word2vec.Train -input wiki.txt -output res.txt -threads 4

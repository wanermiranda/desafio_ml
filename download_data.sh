#!/bin/bash
mkdir -p data
cd data/
wget -c https://s3.amazonaws.com/big-data-public/desafio/desafio.csv.gz && gunzip -f desafio.csv.gz && wc -l desafio.csv
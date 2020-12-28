#!/bin/bash
conda create --force -y --name ml2 python=3.6 && \
conda activate ml2 && \
conda install -y numpy \
		pandas \
		scikit-learn \
		jupyter \
		seaborn \
		statsmodels \
		lightgbm \
		keras \
		autopep8 \
		pylint && \
conda install -y -c conda-forge multicore-tsne	
mkdir -p ./data/exps/

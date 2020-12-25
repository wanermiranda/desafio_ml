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
		pylint && \
conda install -y -c conda-forge multicore-tsne	
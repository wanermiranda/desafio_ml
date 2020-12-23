#!/bin/bash
conda create --force -y --name ml2 python=3.8 && \
conda activate ml2 && \
conda install -y numpy \
		pandas \
		scikit-learn \
		jupyter \
		seaborn \
		statsmodels \
		keras-gpu  \
		tensorflow-gpu \
		lightgbm \
		pylint 
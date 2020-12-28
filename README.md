# Intro
This is a project to takle a challege proposed by the Magazine Luiza team. 
Predict the demand of products for next N months based on a history of previous sales. 

If you want more information you can go to the [Experiments Journal](notebooks/README.md).

## Install
First you download the data needed and unpack it. 
```
$ bash -i download_data.sh 
```
Then you build the environment: 
```
$ bash -i build_env.sh 
```
## Folder Structure 
```
├── build_env.sh
├── download_data.sh 
├── README.md
├── data        # Datasets and intermediate data files.
│   |
│   ├── clean_step1.csv         # During the EDAs, it was the first clean step.
│   ├── clean_step2.csv         # During the EDAs, it was the last clean step.
│   |
│   ├── desafio.csv         # Data provided by the company. 
│   |
│   ├── forecast_dataset_exp11.csv      # Dataset used for prediction experiments. 
│   ├── forecast_dataset_exp12.csv      # Dataset used for prediction experiments. 
│   ├── forecast_dataset_exp13.csv      # Dataset used for prediction experiments. 
│   ├── forecast_dataset_exp14.csv      # Dataset used for prediction experiments. 
│   ├── forecast_dataset_exp1.csv       # Dataset used for prediction experiments. 
│   |
│   ├── output_desafio_exp12.csv        # Dataset with prediction predictions. 
│   ├── output_desafio_exp13.csv        # Dataset with prediction predictions. 
│   ├── output_desafio_exp14.csv        # Dataset with prediction predictions. 
│   |
│   ├── products_features_exp2.csv      # Dataset with product embeddings. 
│   ├── products_features_exp3.csv      # Dataset with product embeddings. 
│   ├── products_features_exp4.csv      # Dataset with product embeddings. 
│   ├── products_features_exp5.csv      # Dataset with product embeddings. 
│   |
│   └── train_val_test.csv      # Train test split by year_month
| 
├── docs        # Documentation and notes
│   ├── Desafio Ciência de Dados - Previsão de Demanda.pdf
│   └── notes.md
│   
├── notebooks               # Experiments - Check the README.md
│   ├── README.md           # Experiment Journal
│   ├── 1. EDA Orders.ipynb
│   ├── 1.1 EDA Orders.ipynb
│   ├── 2. EDA Products.ipynb
│   ├── 3. EDA Correlations.ipynb
│   ├── 4. Clustering - Feature Engineering.ipynb
│   ├── 6. Prediction - Exp 1 DatasetPrep.ipynb
│   ├── 5. Clustering - Exp 1.ipynb
│   ├── 5. Clustering - Exp 2.ipynb
│   ├── 5. Clustering - Exp 3.ipynb
│   ├── 5. Clustering - Exp 4.ipynb
│   ├── 5. Clustering - Exp 5.ipynb
│   ├── 6. Prediction - Exp 1.ipynb
│   ├── 6. Prediction - Exp 2.ipynb
│   ├── 6. Prediction - Exp 4.ipynb
│   ├── 6. Prediction - Exp 5.ipynb
│   ├── 6. Prediction - Exp 6.ipynb
│   ├── 6. Prediction - Exp 7.ipynb
│   ├── 6. Prediction - Exp 8.ipynb
│   ├── 6. Prediction - Exp 9.ipynb
│   ├── 7. Prediction - Exp 10 - Quantile Regression.ipynb
│   ├── 7. Prediction - Exp 11 DatasetPrep.ipynb
│   ├── 7. Prediction - Exp 11.ipynb
│   ├── 7. Prediction - Exp 12 DatasetPrep.ipynb
│   ├── 7. Prediction - Exp 12 - Finetunning.ipynb
│   ├── 7. Prediction - Exp 12.ipynb
│   ├── 7. Prediction - Exp 13 DatasetPrep.ipynb
│   ├── 7. Prediction - Exp 13 - Finetunning.ipynb
│   ├── 7. Prediction - Exp 13.ipynb
│   ├── 7. Prediction - Exp 14 DatasetPrep.ipynb
│   ├── 7. Prediction - Exp 14 - Finetunning.ipynb
│   └── 7. Prediction - Exp 14.ipynb
|
└── src # Helper code
    ├── metrics.py # Metrics and some evaluation for re-use.
    ├── mlp_quantile.py # Neural network with the titled_loss (quantiles)
    ├── optimizer.py # Optimizer used for Clustering - Elbow Method
    └── visualization.py # Visualization for regressions 
```
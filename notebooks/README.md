
# Experiment Journal

This is the experimenting area with the notebooks tracking all steps until the final project. 

Those experiments are organized in 7 chapters described bellow. 

## What could help? 
* Location from each order. 
* Time. 
* Category description to identify if the embeddings were okey. 
* Product description to understand and validate the buying seasons and behaviours.
* It would be better to use a closed whole year, instead of 6 months of each year 2016 and 2017. 
* *The buyer's personas* 
---
## 1 to 4 chapters EDAs 
There are 4 notebooks for EDA. 
### (1, 1.1, 2) EDA Orders
In this first notebook the idea was to understand de fields and remove some more obvious outliers.
#### Insights 
* Look only for orders with the status "entrega total" to avoid training data on cancelled orders or any other unwanted behaviour. 
* Came up with some features: percentual taxes, markup (price/liquid_cost), unit prices and others.
* 178620 orders.
* 99% of the orders contains less or equal 2 products. 
* 90% of the orders contain only 1 product.
* 13% of the sales were cancelled.
* 130 products. 
* 10 Categories. 
* 16 channels. 
* We filtered the 80% of the orders, all of those with the `process_status  == 'entrega total'`. 
* There was a category `388128822cef4b4f102ae881e040a64b` correspoding to 85% of the orders. 
* The same containing 81% of the products and 85% of all items sold.
* Crossing the Products, categories and orders by `revenue, quantity and order numbers`.
#### Categories
* 3 Categories showed to be more prominent `['90cc5bdd050bcd7cf0d50d079d0fda66',
 '9a97178a18aa6333aabdfb21de182b99',
 '388128822cef4b4f102ae881e040a64b',
 'dda10a917a9ea3120e5d299af5105290']`. 
* Compared the behaviour by week_number and month against the whole dataset. 
* The sales peak for the whole orders are on jan, may and november with some increase on dec.
* Category 90cc seems to increase quantities on November, december with a whole year stable. 
* There was a peack on september and november for dda
* 9a9 had peaks on may, august and november, december 
* 388 had peacks on ay and november, january
* Christmas, couples and blackfridays? 
 #### Sources
 * Using the same method of crossing products, orders now with the sources. 
 * The month 6 seems to be the one of least sales for all, except the 98d source. 
* The 152 source has a good performance on the early months of the year. 
* 9d3 is quite non-motonic with some spkies athe march, may, november and jan. 
* cf7 has two spkies at may and november/december.
* 98 has a good spkie around june and november/jan.
* The big spike for b7 is at november and jan. 
* there was no sales for a57 on august? 
---
### 3. EDA Correlations
* We focused more on the most sold products to understand what is different with them. 
* It is interesting to see that also 50% of  the orders/quantity are from 10 Products. 
* The products are selling in orders with 1 quantity 90% of the time.
* The price deviation on 3454ea52396a4cfd3fc37414d30c7b9c and 4534ea61b50410b3b6243e02b40c8cd1 when compared to its means have a higher value than its pairs. 
* The product 4534ea61b50410b3b6243e02b40c8cd1 doesn't have to pay pis/cofins. 
* 75% of the sales for 760693745e10b0c5e68c42214c729b0d doens't do tax substitution.
* The product costs doesn't change much?
* There were some sales with negative revenue (losses) 4534ea61b50410b3b6243e02b40c8cd1 and 2e35421c34fb588ba40a0c57b3971d24. 
* It apears to show some revenue/markup hotspots. 
* there are also a region base for some products when taking account the tax. 
--- 
## 4 and 5. Clustering Feature Engineering
* Following the EDAs the first thing before clustering was to gather all the features possible to come up with. 
* Get dummies for the categorical features (source, category, etc.)
* Resume all the price/order behaviour for the 130 products as a feature vector (std, mean, min, max, percentiles).
### 5. Clustering
Based on some old projects from my masters we used the elbow method to add clusters to the kmeans until the error stopped to fall or it become less than an epsilon value.
* The first experiment was a basic `kitchen-sink` took all the features and throwed then in to see what will happen. Nothing happend, all 130 products were well separated into 130 centroids. 
* The second experiment showed more promising so there was an addition of more reliable comparative metrics: 
    * Davies Bouldin - 
    ```
            The minimum score is zero, with lower values indicating better clustering.
            https://scikit-learn.org/stable/modules/generated/sklearn.metrics.davies_bouldin_score.html
    ```
    * Calinski and Harabaz - 
    ```
            The score is defined as ratio between the within-cluster dispersion and the between-cluster dispersion.
            The score is higher when clusters are dense and well separated, which relates to a standard concept of a cluster.
            https://scikit-learn.org/stable/modules/generated/sklearn.metrics.calinski_harabasz_score.html   
    ```
    * Silhouette Score - 
    ```
    The best value is 1 and the worst value is -1. Values near 0 indicate overlapping clusters. Negative values generally indicate that a sample has been assigned to the wrong cluster, as a different cluster is more similar.
            https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html
    ```

    * 3 metrics, because there is always a metric for a method, 2 of 3 should make you win.

* I'll be using it as an embedding during the forecast. 
* I'm afraid it could take a dataleak into the prediction, in this project, and when in production the idea is to use past events only for this embedding. 

#### Result
* Considering the metrics the experiments ended with 2 potential embeddings for behaviour and seasonality, the experiments 3 (30 clusters) and 4 (10 clusters).
---
### 6. and 7. Predictions
In this moment the real problem starts. 
#### Metrics: 
We used 5  metrics here:
* r^2  - Correlation coefficent between the predicted and  ground truth value.   
* MSE  - Mean Squared Error (y-y_pred) to calculate the mean squared deviation from the predicted value, good to check for outliers since it an Squared Error.

* RMSE - The root of MSE, good to get a more understandable error to the domain.
* MAE - Mean Absolute Error, similar to the RMSE and more understandable but less sentive to outliers.
* MAPE - Mean Absolute Percentage Error, similar to the MAE but here in terms of percentages. 
* MDAPE - Similar to the MAPE but using the median 50% percentile instead of the mean. It shows that 50% of the distribution error is bellow a value. It is good to check regressions overall and more understandable to the customer because it is normalized across any volumes of predictions. 


### Experiments
* At this point I was 2 days from the due date, so I had to make up time.
* There were 14 experiments in total. 
* Starting fixing 4 simple regressors with no fine-tunning: 
    * Decision trees
    * Gradient Boosting
    * Light GBM 
    * RandomForest
* Decided for those because I'm more confortable with their results. Decisions trees require less effort with missing values (nan, null) and are quite faster to train / evaluate.
#### Evaluation Protocol
* The protocol used was a timeseries K fold, resulting in 7 folds. They are implemented in the notebooks with name ending DatasetPrep. 
```
{'set': 0, 
    'train': ['2016-06', '2016-07', '2016-08'], 
    'val': ['2016-09', '2016-10', '2016-11', '2016-12', '2017-01', '2017-02']}
{'set': 1, 
    'train': ['2016-06', '2016-07', '2016-08', '2016-09'], 
    'val': ['2016-10', '2016-11', '2016-12', '2017-01', '2017-02']}
{'set': 2, 
    'train': ['2016-06', '2016-07', '2016-08', '2016-09', '2016-10'], 
    'val': ['2016-11', '2016-12', '2017-01', '2017-02']}
{'set': 3, 
    'train': ['2016-06', '2016-07', '2016-08', '2016-09', '2016-10', '2016-11'], 
    'val': ['2016-12', '2017-01', '2017-02']}
{'set': 4, 
    'train': ['2016-06', '2016-07', '2016-08', '2016-09', '2016-10', '2016-11', '2016-12'], 
    'val': ['2017-01', '2017-02']}
{'set': 5, 
    'train': ['2016-06', '2016-07', '2016-08', '2016-09', '2016-10', '2016-11', '2016-12', '2017-01'], 
    'val': ['2017-02']}
{'set': 6, 
    'train': ['2016-06', '2016-07', '2016-08', '2016-09', '2016-10', '2016-11', '2016-12', '2017-01', '2017-02'], 
    'val': ['2017-03', '2017-04', '2017-05']}
```

* The pair sets from 0 to 5 were used to train the regressors and collect their metrics as average and deviation.
    * Their mean score on all sets is the basis of selection of features during the first 10 experiments. 
* The pair set 6 was reserved as train test for final evaluations. 
    * We used it mostly to see how the regressors will work more closely to the final test june, july and august of 2017. 
### Experiments
* The first experiments were as expected `kitchen-sink` with all features to the table along with all for regressors, the results were as bad as random. But trying to predict the amount of sales without knowing the product. 
* From the experiment 5 onward the product code was added as feature which made the mean r^2 jump from 0.11 to 0.43 on lightgbm, from 0.1 to 0.38 on the randomforest (all Sets 0..5). Although the other metrics were very bad. 
*  With the experiments 7 to 9, we started to check the results also monthly on the set 6, and it showed that the two clustering methods were contributing almost the same to the performance. The choice was then to keep only one the Hierarchical clustering (easier to interpret with the dendogram in future studies).
* Now from the experiment 10 foward we kept the gradient boosting methods focusing on quantiles. 
    * The idea is that the quantile regression could help with the high values of MDAPE, we were missing the values by almost the double of the amount expected.
    * There was also the idea of bringing a little bit of network network to the play. Without success (further notice: use embedding layers could help).
    * The MDAPE improved a bit from 90% to 66% (sets 0..5). The best R2 was still on the verge of 0.45. 
* In the experiment 12 we brought back the `unit_price` feature removed during the early experiments and with the quantile it brought the results up a big more. 
    * Kept the 66% of MDAPE now with a 0.57 r2 on the sets 0..5. 
* With some fine tunning it improved marginally at this point. 
    ```
        Used grid a search training from 2016-06 to 2017-02 and validating against 2017-03, 2017-04 and 2017-05. 
    ```
    * kept the lightgbm and lightgbm with quantiles. 
* The experiments 13 and 14 were to compare the embeddings (10 clusters against 31 clusters). 
* The best result obtained was with the 31 clusters in the experiment 14: 
    * Exp 13: 

|    RMSE    |   MAPE   |   MDAPE  |      MSE     |     MAE    |    R2    |                      reg_inst                     | r_name | set | year_month |
|:----------:|:--------:|:--------:|:------------:|:----------:|:--------:|:-------------------------------------------------:|:------:|:---:|:----------:|
| 170.224393 | 2.668993 | 0.852349 | 28976.344000 | 82.856000  | 0.484495 | LGBMRegressor(max_depth=9, metric='mape', n_es... | gbm    | 6   | 2017-03    |
| 159.561624 | 2.520156 | 0.660550 | 25459.912000 | 70.456000  | 0.547054 | LGBMRegressor(alpha=0.5, max_depth=9, metric='... | gbm_q  | 6   | 2017-03    |
| 135.783458 | 3.127138 | 0.820856 | 18437.147541 | 73.557377  | 0.623034 | LGBMRegressor(max_depth=9, metric='mape', n_es... | gbm    | 6   | 2017-04    |
| 116.744291 | 1.741741 | 0.558451 | 13629.229508 | 59.540984  | 0.721337 | LGBMRegressor(alpha=0.5, max_depth=9, metric='... | gbm_q  | 6   | 2017-04    |
| 200.112799 | 1.956087 | 0.761905 | 40045.132231 | 103.016529 | 0.462891 | LGBMRegressor(max_depth=9, metric='mape', n_es... | gbm    | 6   | 2017-05    |
| 181.566895 | 1.549538 | 0.575758 | 32966.537190 | 87.347107  | 0.557833 | LGBMRegressor(alpha=0.5, max_depth=9, metric='... | gbm_q  | 6   | 2017-05    |

    * Exp 14: 

|    RMSE    |   MAPE   |   MDAPE  |      MSE     |    MAE    |    R2    |                      reg_inst                     | r_name | set | year_month |
|:----------:|:--------:|:--------:|:------------:|:---------:|:--------:|:-------------------------------------------------:|:------:|:---:|:----------:|
| 137.829083 | 2.099851 | 0.777778 | 18996.856000 | 64.520000 | 0.662035 | LGBMRegressor(max_depth=9, metric='mape', min_... | gbm    | 6   | 2017-03    |
| 132.293280 | 1.566074 | 0.645161 | 17501.512000 | 57.576000 | 0.688638 | LGBMRegressor(alpha=0.5, max_depth=21, metric=... | gbm_q  | 6   | 2017-03    |
| 110.498275 | 1.895688 | 0.854167 | 12209.868852 | 62.672131 | 0.750357 | LGBMRegressor(max_depth=9, metric='mape', min_... | gbm    | 6   | 2017-04    |
| 120.300818 | 1.387526 | 0.500000 | 14472.286885 | 58.532787 | 0.704100 | LGBMRegressor(alpha=0.5, max_depth=21, metric=... | gbm_q  | 6   | 2017-04    |
| 154.531550 | 3.350919 | 0.771429 | 23880.000000 | 86.016529 | 0.679707 | LGBMRegressor(max_depth=9, metric='mape', min_... | gbm    | 6   | 2017-05    |
| 146.911622 | 1.560838 | 0.666667 | 21583.024793 | 81.636364 | 0.710516 | LGBMRegressor(alpha=0.5, max_depth=21, metric=... | gbm_q  | 6   | 2017-05    |
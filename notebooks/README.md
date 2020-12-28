
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
--- 

#### Experiments
* At this point I was 2 days from the due date, so I had to make up time.
* There were 14 experiments in total. 
* Starting fixing 4 simple regressors with no fine-tunning: 
    * Decision trees
    * Gradient Boosting
    * Light GBM 
    * RandomForest
* Decided for those because I'm more confortable with their results. Decisions trees require less effort with missing values (nan, null)
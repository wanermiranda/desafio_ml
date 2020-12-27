# Notes
* Theme - Demand prediction
	* How much will we sell in the comming months? 
	* Optimize warehousing costs. 
	* Avoid idle products in the shelves. 
	* Avoid shortage of products in the warehouse.
* Insights
	* Seasonal demand of some products. 
	* Price sensibility. 

* Main target
	* How much of each product we will have to by, avoiding excess and shortage of products. 

* Dataset: 
	`https://s3.amazonaws.com/big-data-public/desafio/desafio.csv.gz`


* Requirements
	1. Clustering (unsupervised)
		- Evaluate the quality of the clustering.
		- Evaluate the semantics of the cluster (characteristics).
		- The better clustering was when reduced the behaviour to months, weekends, pis exception (0, 9.25), sources and categories. 
		- 
	2. Predict the product sales for the next months: 
		- june, july and august
		- Imagine that you don't have a stock and you need to buy everything. 
		- How much of each product type would you buy? 
		- Also Provide the metrics about the model and an essay about the parameters and algorithm.  
	3. Make an analysis of your reports and an essay about it. 
		- Is there any data that when provided could help?



* Evaluation criterias
	* Problem comprehension and solution design. 
	* Research capabilities to solve the question. 
	* Using of algorithms for prediction and classification. 
	* Capacity to transmit complex knowledge in a simple way; Comunication with people outside the academic/tech world. 




## Notes on the clustering 
	- During the EDA it was possible to see that the month of may is a great separator and, it returned again during the clustering, when 5 / 10 showed it as a proeminent feature. 
	- January and march also appeared in the same way, separating 6/10 
	- The channels played another huge part, one cluster (5) was characterized by the existence of a particular channel. 
	- The tax exception was also a separation, probably because of the characteristics of the product.
	- The weekd behaviour was kind courious also, but not so proeminent. 
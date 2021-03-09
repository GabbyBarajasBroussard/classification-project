# Predicting Churn at Telco
## About the project
### Goals
#### The goal for this project is to create a model predicting churn using the data obtained from the Telco databas by identifying what conditions and attributes are the largest drivers of churn. The deliverables from this project are acquire.py, prepare.py, telco.csv and final_presentation.ipynb. 


## Data Dictionary
| Terminology         | Definition                                                                                                                                                                                                                                                                                                                           |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Churn               | The measure of the number of individuals moving out of a collection group over a specific period of time.                                                                                                                                                                                                                            |
| Logistic Regression | A regression algorithm used to predict discrete outcomes.                                                                                                                                                                                                                                                                            |
| Decision Tree       | A sequence of rules that can be used to classify 2 or more classes using supervised machine learning processes.                                                                                                                                                                                                                      |
| Random Forest       | A learning method that constructs a multitude of decision trees at training time and outputting the classification.                                                                                                                                                                                                                  |
| K Nearest Neighbor  | A "lazy" algorithm in that it does not attempt to construct a general internal model, but simply stores instances of the training data. Classification is computed from a simple majority vote of the k nearest neighbours of each point. Makes predictions based on how close a new data point is to known data points. Precision:  |
| Precision           |                                                                                                                                                                                                                                                                                                                                      |
| Recall              | If this score is high, you didn’t miss a lot of positives. But as it gets lower, you are not predicting the positives that are actually there. tp / (tp + fn)                                                                                                                                                                        |
| F1 Support          | The balanced harmonic mean of Recall and Precision, giving both metrics equal weight. The higher the F-Measure is, the better.                                                                                                                                                                                                       |
| Support             | The number of occurrences of each class in where y is true.                                                                                                                                                                                                                                                                          |
| Alpha               | Alpha is the likelihood that a true population parameter lays outside the confidence interval.                                                                                                                                                                                                                                       |
| Confidence Interval | The probability that a population parameter will fall between a set of values for a certain proportion of times.                                                                                                                                                                                                                     |
<br>

## Hypothesis Testing
    First Hypothesis 𝐻$0$ :  
    𝐻𝑎 : 
    alpha ( 𝛼 ): 1 - confidence level (95% confidence level -> 𝛼=.05 )


    Second Hypothesis
    𝐻0 : 
    𝐻𝑎 : 
    alpha ( 𝛼 ): 1 - confidence level (95% confidence level -> 𝛼=.05 )

## Data Science Pipeline Used
### acquire.py
<ol>
<li>acquire data from csv gathered from sql. </li>
</ol><br>
### prepare.py
<ol>
<li> address missing data </li>
<li> address outliers </li>
<li> split into train, validate, test</li>
</ol><br>
### explore
<ol>
<li> plot correlation matrix of all variables </li>
<li> test each hypothesis </li> 
</ol><br>
### model
<ol>
<li> try different algorithms: decision tree, logistic regression, random forest,knn</li> 
<li> which features are most influential? </li>
<li> evaluate on train </li>
<li> select top 3 +/- models to evaluate on validate </li>
<li> select top model </li>
<li> run model on test to verify. </li>
 </ol><br>
### conclusion
<ol>
<li> summarize findings </li>
<li> make recommendations </li>
<li> next steps </li>
<li> how to run with new data. </li> 
</ol><br><br>

## Conclusion

<ul>
<li>Clients who are non-seniors, who have premium features such a streaming, security features and support features are more likely to churn and they are paying a higher monthly cost. Clients who either have a partner or a family also are likely to pay more. 
 <li> Through analyzing the data, we have found that the customers who churn are paying more. This can be explained by the additional features that many customers have.
 <li> If more time was allotted,  the data science team would evaluate which contract option has the highest amount of churn.
 <li> Next steps would be to find out what each specific features cost, evaluate which group of non-seniors are churning (ie. college age vs middle adult) and what competitors pricing for similar features are.
<li> My recommendation to retain customers would be to investigate offering bundle deals and having customers sign contracts to reduce the churn with the company.

## How to reproduce the results
#### You may download acquire.py and prepare.py. You will need your own env.py file with your SQL credentials in order to access the SQL server.

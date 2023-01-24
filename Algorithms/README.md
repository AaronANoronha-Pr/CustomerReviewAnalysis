
# Algorithms

The dataset has about 960,049 rows of data. There are some null values. We simply  get rid of those null values.
As the dataset is pretty big, it takes a lot of time to run some machine learning algorithm. So, we have used 5% of the data for this project which is still 48,002 data.
We have added a new column named ‘sentiments’ to the dataset that will use 1 for the negative reviews and 2 for the nutral reviews and 3 for positive reviews.
 
Sentiment analysis uses computational tools to determine the emotional tone behind words. Python has a bunch of handy libraries for statistics and machine learning so in this project we have use Scikit-learn.

Scikit-learn is a Python module with built-in machine learning algorithms.
We have used two popular vectorizers  count vectorizer and TF-IDF vectorizer to vectorize the text data in the review column and then use three different classification models from scikit-learn models. 

The classifiers that we have used are :
 1. Logistic Regression  
 2. Support Vector Machine 
 3. K Nearest Neighbor Classifier


## Accuracy
| ALGORITHMS|ACCURACY|
|:-----------------|:---|
|Logistic Regression with CountVectoriser |0.8240489979584183|
|SVM with CountVectoriser|0.8182992375317695|
|KNN with CountVectoriser|0.7699679180034166|
|Logistic Regression with TF-IDF Vectoriser|0.8327986333902754|
|SVM with TF-IDF Vectoriser|0.8288404649806258|
|KNN with TF-IDF Vectoriser|0.7803424857297613|
|Random Forest|0.718|
|Naive Bayes|0.7765509770426232|
|Neural Network + word Embedding | 0.9375694857215595|

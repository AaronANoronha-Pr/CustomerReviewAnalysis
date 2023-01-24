# Experiments

- Before selecting a model, it is important to conduct experiments with different models and different embedding layers to determine which one performs the best. 
We tried different architectures, hyperparameters and pre-trained models to see which one performs the best. 
It is a good practice to evaluate the models using different evaluation metrics, such as accuracy, precision, recall, F1 score etc.

- Another important factor when selecting a model is the computational resources available. Some models are computationally expensive and may require powerful hardware 
to run effectively. It's important to consider the computational resources available when selecting a model and choose one that can be run effectively on the 
available resources.


S no. | Experiement | Result | Conlusion | Link 
--- | --- | --- | --- |--- 
1 | universal-sentence-encoder-large (Neural Network + word Embedding) | accuracy: 0.9358, val_accuracy: 0.9302| Generalized Model, working well | [Notebook](https://github.com/AaronANoronha/CustomerReviewAnalysis/blob/main/Experiments/Universal_Sentence_Encoder_%2B_2_layer.ipynb) 
2 | Multinomial Model | accuracy:0.835| Proballistic Model, Working well but low accuracy |
3|Logistic Regression with CountVectoriser | accuracy:0.8240489979584183|
4|SVM with CountVectoriser| accuracy:0.8182992375317695|
5|KNN with CountVectoriser| accuracy:0.7699679180034166|
6|Logistic Regression with TF-IDF Vectoriser| accuracy:0.8327986333902754|
7|SVM with TF-IDF Vectoriser| accuracy:0.8288404649806258|
8|KNN with TF-IDF Vectoriser| accuracy:0.7803424857297613|
9|Random Forest| accuracy:0.718|
10|Naive Bayes| accuracy:0.7765509770426232|

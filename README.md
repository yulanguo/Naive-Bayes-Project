
# Naive Bayes Sentiment Classifier

This project implements a Naive Bayes classifier from scratch to perform sentiment classification on movie reviews. The classifier is trained to distinguish between positive and negative reviews.

### Methods

- `train(lines)`  
  Trains the classifier using text input.

- `classify(lines)`  
  Predicts sentiment as positive, negative, or neutral.

### Main.py

- Loads full dataset from `alldata.txt`  
- Trains the classifier on the first 12,478 samples  
- Classifies the remaining samples  
- Calculates F-scores  
- Uses `unittest` to assert that the model meets performance thresholds

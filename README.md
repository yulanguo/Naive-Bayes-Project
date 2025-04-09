
# Naive Bayes Sentiment Classifier

This project implements a Naive Bayes classifier from scratch to perform sentiment classification on movie reviews.  
The classifier is trained to distinguish between positive and negative reviews using word frequencies and probabilistic modeling.

---

### Methods

- `train(lines)`  
  Trains the classifier using labeled text input.

- `classify(lines)`  
  Predicts sentiment for a list of reviews.

---

## Evaluation Script

**File:** `main.py`

This script evaluates the performance of the classifier:

- Loads full dataset from `alldata.txt`  
- Trains the classifier on the first 12,478 samples  
- Classifies the remaining samples  
- Calculates F-scores  
- Uses `unittest` to assert that the model meets performance thresholds

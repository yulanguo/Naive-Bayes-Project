#  Naive Bayes Sentiment Classifier

This project implements a **Naive Bayes classifier** from scratch to perform **binary sentiment classification** on a custom dataset. The classifier is trained to distinguish between positive and negative text entries using word frequencies and probabilistic modeling.


## Classifier Details

###  `Bayes_Classifier` (in `student_code.py`)

A custom implementation of the Naive Bayes algorithm with:

- Bag-of-words model
- Laplace smoothing
- Separate word counts for each class

#### Methods:

- `train(lines)`  
  Trains the classifier using labeled text input (`"5"` or `"1"` as labels).

- `classify(lines)`  
  Predicts sentiment for a list of input lines. Returns:
  - `"5"` if more likely positive  
  - `"1"` if more likely negative  
  - `"0"` if equal probability

---

## Evaluation Script

### `main.py`

- Loads full dataset (`alldata.txt`)
- Trains classifier on first 12,478 samples
- Classifies the rest
- Calculates F-scores using a custom function
- Asserts model passes performance thresholds using `unittest`

#### F-score Thresholds:

- F-score for `"5"` (positive): **> 0.90**
- F-score for `"1"` (negative): **> 0.60**

---

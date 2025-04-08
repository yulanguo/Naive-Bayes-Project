# Naive-Bayes-Project
CS 348 Assignment:
Naive Bayes Movie Classifier 

## Bayes_Classifier

This is a simple **Naive Bayes classifier** for binary sentiment classification. It classifies text as either **positive ("5")** or **negative ("1")** based on the frequency of words observed during training.

---

### 🛠️ How It Works

#### `train(lines)`
- Accepts a list of strings, each formatted as `label|metadata|text`.
- Parses each line to:
  - Split the input text into individual words.
  - Count occurrences of each word within each class (positive or negative).
  - Track the total number of documents and words in each class.
  - Build a global vocabulary set of all seen words.

#### `classify(lines)`
- Accepts a list of strings in the same format as training data.
- For each line:
  - Applies Laplace smoothing to avoid zero probabilities for unseen words.
  - Calculates the log-likelihood of the text belonging to the positive and negative classes.
  - Compares probabilities:
    - Predicts `"5"` if the positive class probability is higher.
    - Predicts `"1"` if the negative class probability is higher.
    - Predicts `"0"` if probabilities are equal.

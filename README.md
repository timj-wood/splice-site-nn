# Can a tiny neural network learn where a gene is spliced?

A beginner's machine-learning mini-project in bioinformatics: from logistic regression, to a single
artificial neuron trained with hand-written gradient descent, to a small multi-layer perceptron in
PyTorch — all on 3,190 short DNA sequences from the classic UCI splice-junction dataset.

![What a single neuron learned](figures/02_neuron_weights.png)

*The 240 weights of one neuron trained to spot a splice junction, laid out by position and base.
Nobody told it about biology, yet the strongest weights are **AG** just before the junction and
**GT** just after — the textbook intron boundary.*

## Results

| model | test accuracy (798 sequences) |
|---|---|
| k-nearest neighbours (k chosen by cross-validation) | 0.851 |
| logistic regression | 0.937 |
| single neuron, gradient descent written by hand (splice site vs none) | 0.934 |
| same neuron via PyTorch autograd | 0.934 (identical weights) |
| MLP, one hidden layer of 32 ReLU units | 0.940 |

The headline isn't the last row. It's that (1) the hand-derived gradient and autograd give the same
answer to 7 decimal places, so backpropagation stops being a black box, and (2) a model with no
biological prior rediscovers the GT…AG consensus. The MLP's loss curve also shows textbook
overfitting after a few epochs — a useful thing to see for yourself.

## Contents

```
data/splice.data               the dataset (UCI, CC BY 4.0) — see data/README.md
src/splice_utils.py            load the file, one-hot encode sequences, name features
notebooks/01_baseline_sklearn.ipynb     logistic regression + kNN baseline, weight heatmap
notebooks/02_perceptron_to_mlp.ipynb    neuron by hand → autograd → MLP → position importance
figures/                       every plot the notebooks produce
blog/post_outline.md           skeleton for the accompanying blog post
```

## Running it

```bash
python -m venv .venv && source .venv/bin/activate     # optional
pip install -r requirements.txt
jupyter lab                                           # then open notebooks/01_… and 02_…
```

Both notebooks run in well under a minute on a laptop CPU. Random seeds are fixed, so you should
reproduce the numbers above exactly (PyTorch may differ in the last decimal place across versions).

## What this builds on

* Jean Golding Institute, [Introduction to Data Analysis in Python (Part 2)](https://bristol-training.github.io/data-analysis-python-2/) — notebook 01 uses nothing beyond this course.
* Jean Golding Institute, [Introduction to AI](https://bristol-training.github.io/intro-to-ai/) — notebook 02 follows its ladder: perceptron → activation → gradient descent → backprop → MLP.
* Steven Morse, [Neural Networks for a beginner (Part I: theory)](https://stmorse.github.io/journal/Beginner-NN-Part-I.html) — the maths. Morse's post is about regression with squared error; notebook 02 swaps in a sigmoid/softmax output and cross-entropy loss for classification and shows how the chain rule simplifies.
* Noordewier, Towell & Shavlik (1991), *Training knowledge-based neural networks to recognize genes in DNA sequences*, NeurIPS — the paper the dataset was built for.

## Data

Molecular Biology (Splice-junction Gene Sequences), UCI Machine Learning Repository,
https://doi.org/10.24432/C5M888 (CC BY 4.0). A copy is included so the notebooks run offline.

# Blog post outline — "Can a tiny neural network learn where a gene is spliced?"

Target: ~1,000 words, 4 figures, written for someone one step behind you. The numbers below come
straight from the notebooks; the prose is yours to write. Suggested figure for each section is in
brackets.

## 1. Why splice sites? (≈120 words)
- One-line biology: introns are cut out of pre-mRNA; almost every intron starts GT and ends AG.
- Why that makes it a good first ML problem: the answer is *known*, so you can check whether the
  model learned biology or noise. 3,190 sequences, 60 bases each, three labels (EI / IE / N).
- Honest framing: this is my first neural network; the aim is to understand it, not to beat anyone.

## 2. Letters → numbers (≈100 words)
- One-hot encoding, 60 × 4 = 240 features. Mention the ambiguity codes and the ⅓, ⅓, ⅓ trick in one sentence.

## 3. The baseline nobody should skip (≈150 words) [figures/01_logreg_weights.png]
- Logistic regression: 0.937 test accuracy. kNN: 0.851 (and why one-hot vectors are rarely "near").
- The weight heatmap already shows GT at +1/+2 for EI and AG at −2/−1 for IE. Say this plainly:
  the linear model found the consensus.

## 4. One neuron, by hand (≈200 words) [figures/02_neuron_two_ways.png]
- Aggregate → activate (link Morse). Sigmoid, cross-entropy, and the fact that the chain rule
  collapses to ∂ℓ/∂z = a − y. Twelve lines of code, no autograd. 0.934 accuracy.
- Then the same thing with `loss.backward()`: identical loss curve, weights agree to 2e−7.
  "Backprop is the chain rule, done systematically" is the sentence to land.

## 5. What the neuron learned (≈120 words) [figures/02_neuron_weights.png]
- The payoff figure. Top weights: −1:G, −2:A, +2:T, +1:G. Nobody told it about introns.

## 6. Adding a hidden layer (≈180 words) [figures/02_mlp_training.png]
- 240 → 32 ReLU → 3, mini-batch SGD, 40 epochs. 0.940 vs 0.937 — basically a tie.
- The loss curve: train keeps falling, test turns up after ~7 epochs. Name it: overfitting.
- The 1991 paper that built this dataset found backprop ≈ their best method too. A mostly additive
  signal doesn't need a deep model; that's a result, not a disappointment.

## 7. What I'd do next (≈100 words)
- Learning-rate sweep, early stopping, a second layer — each is a one-line change.
- A short, honest paragraph on what surprised you (my guess: how little the hidden layer bought,
  and how clean the weight map was).

## Links
- Repo: github.com/timj-wood/splice-site-nn (or whatever you name it)
- JGI courses: Data Analysis in Python part 2; Introduction to AI
- Morse, Neural Networks for a beginner (Part I: theory)
- UCI dataset DOI 10.24432/C5M888

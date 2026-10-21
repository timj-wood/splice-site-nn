"""Small helpers shared by the two notebooks.

Everything here is explained step by step in notebooks/01_baseline_sklearn.ipynb;
it lives in a module so that notebook 02 can reuse it without copy-pasting.
"""

from pathlib import Path

import numpy as np
import pandas as pd

BASES = ["A", "C", "G", "T"]

# IUPAC ambiguity codes that appear in this dataset (only 60 of 191,400 positions).
# Each is spread evenly over the bases it could be, so a "D" becomes 1/3 A, 1/3 G, 1/3 T.
AMBIGUOUS = {
    "D": ["A", "G", "T"],
    "N": ["A", "C", "G", "T"],
    "S": ["C", "G"],
    "R": ["A", "G"],
}

# Position labels: the dataset runs from -30 to +30 with no position 0,
# so the candidate splice junction sits between index 29 (-1) and index 30 (+1).
POSITIONS = list(range(-30, 0)) + list(range(1, 31))


def load_splice(path="data/splice.data"):
    """Load the UCI splice-junction file into a tidy DataFrame.

    Columns: label (EI / IE / N), name, sequence (60-letter string).
    """
    path = Path(path)
    rows = []
    with path.open() as fh:
        for line in fh:
            label, name, seq = [field.strip() for field in line.strip().split(",")]
            rows.append((label, name, seq))
    df = pd.DataFrame(rows, columns=["label", "name", "sequence"])
    assert df["sequence"].str.len().eq(60).all(), "every sequence should be 60 bases long"
    return df


def one_hot(sequences):
    """Turn a list of 60-letter DNA strings into a (n, 240) float array.

    Position p of the sequence occupies columns 4p .. 4p+3 in the order A, C, G, T.
    """
    seqs = list(sequences)
    n, L = len(seqs), len(seqs[0])
    X = np.zeros((n, L * len(BASES)), dtype=np.float32)
    for i, seq in enumerate(seqs):
        for p, letter in enumerate(seq):
            if letter in BASES:
                X[i, 4 * p + BASES.index(letter)] = 1.0
            else:
                options = AMBIGUOUS[letter]
                for b in options:
                    X[i, 4 * p + BASES.index(b)] = 1.0 / len(options)
    return X


def feature_names():
    """Human-readable name for each of the 240 one-hot columns, e.g. '+1:G'."""
    return [f"{pos:+d}:{b}" for pos in POSITIONS for b in BASES]

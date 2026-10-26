"""
Small helpers shared by the two notebooks.

Everything here is explained step by step in scripts/01_baselines.ipynb;
it lives in a module so that notebook 02 can reuse it without copy-pasting.
"""

from pathlib import Path

import numpy as np
import pandas as pd

BASES = ["A", "C", "G", "T"]

# Position labels: the dataset runs from -30 to +30 with no position 0,
# so the candidate splice junction sits between index 29 (-1) and index 30 (+1).
POSITIONS = list(range(-30, 0)) + list(range(1, 31))


def load_splice(path="data/splice.data"):
    """Load the UCI splice-junction file into a tidy DataFrame.

    Columns: label (EI / IE / N), name, sequence (60-letter string).

    Loading code adapted from dna_sequence_analysis.ipynb in:
    https://github.com/Ajayraj18-byte/dna_sequence_analysis_1
    
    Data: UCI Molecular Biology (Splice-junction Gene Sequences)
    https://archive.ics.uci.edu/dataset/69/molecular+biology+splice+junction+gene+sequences
    """
    dataset_file = Path(path)
    if not dataset_file.is_file():
        raise FileNotFoundError(dataset_file)

    df = pd.read_csv(
        dataset_file,
        names=["class", "instance", "sequence"],
        sep=",",
        skipinitialspace=True,
        dtype=str,
    )
    for column in ["class", "instance", "sequence"]:
        df[column] = df[column].str.strip()
    df["sequence"] = df["sequence"].str.upper()

    df = df.rename(columns={"class": "label", "instance": "name"})
    assert df["sequence"].str.len().eq(60).all(), "every sequence should be 60 bases long"
    return df


def one_hot_encode(seq):
    """Turn one DNA string into a flat one-hot array (A, C, G, T per position).

    Bases other than A/C/G/T (the ambiguity codes D, N, S, R) become all zeros.

    Source: https://github.com/angai4/dna-one-hot-encoder/tree/main
    """
    mapping = {
        "A": [1.0, 0.0, 0.0, 0.0],
        "C": [0.0, 1.0, 0.0, 0.0],
        "G": [0.0, 0.0, 1.0, 0.0],
        "T": [0.0, 0.0, 0.0, 1.0],
        "N": [0.0, 0.0, 0.0, 0.0],
    }
    arr = np.array([mapping.get(b, mapping["N"]) for b in seq.upper()], dtype=np.float32)
    return arr.flatten()

def feature_names():
    """Human-readable name for each of the 240 one-hot columns, e.g. '+1:G'."""
    return [f"{pos:+d}:{b}" for pos in POSITIONS for b in BASES]
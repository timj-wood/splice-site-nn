# Data

`splice.data` — Molecular Biology (Splice-junction Gene Sequences), UCI Machine Learning Repository.
DOI: https://doi.org/10.24432/C5M888 · Licence: CC BY 4.0 · 3,190 rows, no missing values.

Each line is `label, instance name, 60-base sequence`:

```
EI,    ATRINS-DONOR-521,    CCAGCTGCATCACAGGAGGCCAGCGAGCAGGTCTGTTCCAAGGGCCTTCGAGCCAGTCTG
```

* `EI` (767) — exon→intron boundary, i.e. a donor site
* `IE` (768) — intron→exon boundary, i.e. an acceptor site
* `N` (1655) — neither

Positions run from −30 to +30 with no position 0; the candidate junction sits between −1 and +1.
Sixty positions in total use IUPAC ambiguity codes: `D` = A/G/T, `N` = any, `S` = C/G, `R` = A/G.
`src/splice_utils.one_hot` spreads these evenly over the possible bases.

To fetch a fresh copy instead of using this one:

```python
from ucimlrepo import fetch_ucirepo
splice = fetch_ucirepo(id=69)
```

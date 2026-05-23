# Semantic Sentence Similarity for Slovak

Experimental NLP system for semantic sentence similarity in Slovak language using dynamically generated concept trees and graph-based similarity metrics.

## Overview

The project computes semantic similarity between Slovak sentences using:
- concept hierarchies,
- synonym relationships,
- semantic distance metrics,
- and multiple aggregation strategies.

For every sentence pair, the system dynamically builds a semantic concept tree from extracted lemmas and computes similarity scores between words and sentences.

The implementation includes:
- Wu-Palmer similarity,
- shortest path similarity,
- Leacock-Chodorow similarity,
- multiple matching strategies,
- configurable aggregation methods,
- parameter evaluation using Pearson correlation.

## Project Structure

```text
api_utils.py               # API communication and concept tree generation
dataset_utils.py           # Dataset loading and train/test split
similarity.py              # Similarity computation logic
tree.py                    # Tree structure and similarity metrics

experiment.py              # Parameter experiments
pearson_eval.py            # Pearson evaluation of configurations
final_test.py              # Final evaluation using best configuration
analyze_correlation.py     # Correlation analysis of parameters

sick_sk.txt                # Slovak SICK dataset
stsbenchmark_sk.txt        # Slovak STS Benchmark dataset

experiment_scores_final_final.json
pearson_results_final_final.csv

concept_cache.json
lemma_cache.json
```

## Similarity Metrics

Implemented semantic similarity metrics:
- Wu-Palmer
- Shortest Path
- Leacock-Chodorow

## Matching Strategies

- one_to_many
- all_to_all
- element_wise

## Aggregation Methods

Word-level aggregation:
- max
- avg
- min

Sentence-level aggregation:
- max
- avg
- min

## Features

- Dynamic semantic concept trees
- Symmetric and directional similarity
- Configurable score exponentiation
- Index-based weighting
- Pearson correlation evaluation
- Stratified dataset split
- Local API response caching

## Requirements

Install dependencies:

```bash
pip install scipy scikit-learn pandas matplotlib requests sympy
```

## API Credentials

The project requires access credentials for the KINIT API.

Create a local file named:

```text
udaje.txt
```

with the following format:

```text
your_email your_password
```

This file is ignored by `.gitignore` and is not included in the repository.

## Running Experiments

Run parameter experiments:

```bash
python experiment.py
```

Evaluate Pearson correlations:

```bash
python pearson_eval.py
```

Run final evaluation:

```bash
python final_test.py
```

Analyze parameter correlations:

```bash
python analyze_correlation.py
```

## Best Configuration

Best experimental configuration achieved approximately:

```text
Pearson ≈ 0.5579
```

using:
- matching = one_to_many
- word aggregation = max
- sentence aggregation = avg
- direction = symmetric
- power = 7
- local exponentiation
- Wu-Palmer similarity

## Notes

The repository contains cached API responses (`concept_cache.json` and `lemma_cache.json`) to reduce the number of external requests and speed up experiments.

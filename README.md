# Bloom Filter Project

## Overview

This project implements a **Bloom Filter**, a probabilistic data structure that efficiently tests whether an element is a member of a set. While it provides fast lookups and space efficiency, it can result in **false positives** (indicating an element might exist when it doesn't). However, it guarantees no **false negatives** (it will never say an element is absent if it’s present).

The program reads two CSV files:
1. **Dataset file**: Used to build the Bloom Filter.
2. **Query file**: Used to test whether each element is likely in the set.

The output indicates if each queried element is "Probably in the DB" or "Not in the DB."

---

## Features

- **Dynamic Bloom Filter Construction**: Automatically calculates the optimal size and number of hash functions based on the dataset size and the desired false-positive probability.
- **Customizable Hashing**: Uses a seed-based custom hash function for generating hash values.
- **Bit Manipulation**: Efficient bit-level operations to manage the bit array.
- **CSV File Integration**: Reads data from CSV files for building and querying the Bloom Filter.

---

## Files in the Project

1. **`main.py`**: The primary Python script containing the Bloom Filter implementation.
2. **Dataset file (CSV)**: The input file to build the filter (e.g., `dataset.csv`).
3. **Query file (CSV)**: The input file to test against the filter (e.g., `query.csv`).

---

## Installation and Usage

### Prerequisites

- Python 3.7 or higher.
- The `csv` and `math` modules (built into Python).
- A terminal or command-line interface.

### Running the Project

1. **Prepare the input files**:
   - **Dataset file**: The first column should contain the elements to include in the Bloom Filter. The first row is treated as a header and ignored.
   - **Query file**: The first column should contain elements to check against the Bloom Filter. The first row is treated as a header and ignored.

2. **Run the script**:
   ```bash
   python main.py <dataset_file> <query_file>

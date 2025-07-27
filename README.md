# Quicksort Algorithm: Deterministic vs Randomized

## Overview
This project compares two implementations of the Quicksort algorithm:

- **Deterministic Quicksort**: Uses the last element of the array as the pivot.
- **Randomized Quicksort**: Chooses a pivot randomly to avoid worst-case partitioning.

The goal is to analyze how randomization affects performance, particularly on sorted and reverse-sorted arrays.

## Project Structure

| File                     | Description                                      |
|--------------------------|--------------------------------------------------|
| `deterministic_quicksort.py` | Quicksort with fixed (last element) pivot       |
| `randomized_quicksort.py`    | Quicksort with randomized pivot selection       |
| `performance_test.py`        | Script to measure and compare run times         |
| `Quicksort_Assignment_Report.docx` | Full report with charts, table, and discussion |
| `deterministic_timing.png`   | Bar chart of deterministic performance          |
| `randomized_timing.png`      | Bar chart of randomized performance             |

## How to Run

To execute the performance comparison:

```bash
python performance_test.py

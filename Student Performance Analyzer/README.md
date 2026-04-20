# Student Performance Analyzer (NumPy Project)

## Overview

This project analyzes student performance data using NumPy. It focuses on data cleaning, transformation, and analytical operations on a dataset containing missing values.

The project simulates a real-world academic dataset and demonstrates how to extract meaningful insights using efficient array operations.

---

## Objectives

- Handle missing values in student marks
- Perform row-wise and column-wise analysis
- Dynamically expand dataset with new students and subjects
- Identify top performers and difficult subjects
- Apply normalization and data transformations

---

## Dataset Description

The dataset represents marks of students across different subjects.

- Rows represent students
- Columns represent subjects:
  1. Math
  2. Science
  3. English
  4. Computer

Missing values are present and handled during preprocessing.

---

## Key Features

### 1. Missing Value Handling

- Detects NaN values
- Replaces them using column-wise mean
- Uses NumPy functions such as `np.nanmean`, `np.where`, and `np.take`

---

### 2. Data Expansion

- Adds a new student (row-wise)
- Adds a new subject (column-wise)
- Maintains correct array structure using reshape and concatenate

---

### 3. Performance Analysis

- Calculates total marks per student
- Calculates average marks per subject
- Identifies top-performing student
- Identifies toughest subject

---

### 4. Data Transformation

- Applies bonus marks using broadcasting
- Normalizes data between 0 and 1

---

### 5. Data Splitting

- Splits dataset into subsets for further analysis

---

## Business / Analytical Questions Solved

1. How can missing marks be handled efficiently?
2. Which student has the highest total marks?
3. Which subject is the most difficult?
4. How does adding new data affect analysis?
5. How can student marks be normalized for comparison?

---

## Concepts Used

- NumPy array manipulation
- Handling missing values
- Broadcasting
- Reshaping arrays
- Concatenation (row-wise and column-wise)
- Axis-based operations
- Statistical functions (mean, sum, argmax, argmin)
- Data normalization
- Array splitting

---

## Learning Outcomes

- Strong understanding of NumPy operations
- Ability to handle incomplete datasets
- Improved understanding of row vs column operations
- Practical knowledge of vectorized computation
- Foundation for data analysis workflows

---

## Tech Stack

- Python
- NumPy

---

## Future Improvements

- Add advanced analytics (subject ranking, consistency check)
- Integrate with Pandas for real datasets
- Visualize results using Matplotlib

---

## Author

Sarthak Jain

---

## Note

This project is built for learning purposes and demonstrates how NumPy can be used for efficient data preprocessing and analysis.

# E-Commerce Sales Analyzer (NumPy Project)

## Overview

This project is a NumPy-based data analysis system that simulates an e-commerce sales dataset. It focuses on real-world data preprocessing, transformation, and analytical operations such as handling missing values, feature expansion, and performance evaluation.

The goal of this project is to demonstrate how raw and incomplete data can be transformed into meaningful insights using efficient NumPy operations.

---

## Objectives

- Clean and preprocess raw sales data containing missing values
- Perform row-wise and column-wise analysis
- Expand dataset dynamically by adding new rows and columns
- Apply vectorized operations for performance improvement
- Extract business insights such as best-selling product and highest sales day

---

## Key Features

### 1. Missing Value Handling
- Detects missing values (NaN)
- Replaces them using column-wise mean
- Uses NumPy indexing and advanced selection techniques

### 2. Dynamic Data Expansion
- Adds new sales entries as additional rows (new days)
- Adds new product data as additional columns
- Maintains consistent array structure using reshape and concatenate

### 3. Sales Analysis
- Calculates total sales per day
- Calculates total sales per product
- Identifies best-performing product
- Identifies highest sales day

### 4. Data Transformation
- Applies discount using vectorized broadcasting
- Normalizes dataset values between 0 and 1

### 5. Data Splitting
- Splits dataset for segmented analysis using vertical splitting

---

## Concepts Used

- NumPy arrays
- Broadcasting
- Reshaping arrays
- Concatenation (row-wise and column-wise)
- Axis-based operations
- NaN handling (np.nanmean, np.where, np.take)
- argmax and argmin functions
- Normalization techniques
- Array splitting (vsplit)

---

## Dataset Description

The dataset represents:
- Rows: Days of sales
- Columns: Products
- Values: Sales amount
- Missing values represent incomplete records

---

## Business Questions Solved

1. How do we handle missing sales data efficiently?
2. Which product has the highest total sales?
3. Which day recorded the highest revenue?
4. How does discount affect overall sales distribution?
5. How can we normalize sales data for comparison?
6. How does adding new products or days affect analysis?

---

## Insights Gained

- Data cleaning is essential before analysis
- Column-wise statistics are important for business decisions
- Broadcasting simplifies bulk operations
- Proper array shaping is critical for combining datasets
- Real-world data is dynamic and continuously expanding

---

## Technical Stack

- Python
- NumPy

---

## Learning Outcome

By completing this project, the following skills are developed:

- Strong understanding of NumPy array manipulation
- Ability to handle missing data effectively
- Understanding of real-world data analysis flow
- Confidence in using vectorized operations instead of loops
- Foundation for moving into Pandas and Machine Learning

---

## Future Improvements

- Integration with Pandas for better data handling
- Visualization of sales trends using Matplotlib
- Real-time data input simulation
- Conversion into a full data analytics pipeline

---

## Author

Sarthak Jain

---

## Note

This project is purely for learning purposes and demonstrates how NumPy can be used to simulate real-world business analytics problems.

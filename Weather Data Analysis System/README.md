# Weather Data Analysis System (NumPy Project)

## Overview

This project focuses on analyzing weather data using NumPy. It simulates real-world environmental data containing missing values and performs data cleaning, transformation, and analysis.

The project demonstrates how raw weather data can be processed into meaningful insights using efficient array operations.

---

## Objectives

- Handle missing weather data using statistical methods
- Perform row-wise and column-wise analysis
- Dynamically expand dataset with new records and features
- Apply vectorized operations for efficient computation
- Extract useful insights such as extreme weather conditions

---

## Dataset Description

The dataset represents weather conditions across multiple days.

- Rows represent different days
- Columns represent weather features:
  1. Temperature (°C)
  2. Humidity (%)
  3. Wind Speed (km/h)
  4. Rainfall (mm)

Missing values are present and must be handled before analysis.

---

## Key Features

### 1. Missing Value Handling

- Detects NaN values in the dataset
- Replaces missing values using column-wise averages
- Uses NumPy functions such as `np.nanmean`, `np.where`, and `np.take`

---

### 2. Data Expansion

- Adds a new day of weather data (row-wise expansion)
- Introduces a new feature (Air Quality Index) as a column
- Ensures proper shape alignment using reshape and concatenate

---

### 3. Daily Analysis

- Calculates average weather conditions per day
- Computes total weather intensity per day

---

### 4. Feature Analysis

- Computes average value of each weather feature
- Identifies the feature with the highest overall value

---

### 5. Extreme Condition Detection

- Finds the day with highest temperature
- Finds the day with lowest humidity

---

### 6. Data Transformation

- Adjusts temperature and humidity using broadcasting
- Applies normalization to scale data between 0 and 1

---

### 7. Data Splitting

- Splits dataset into subsets for further analysis
- Uses slicing and NumPy split functions

---

## Concepts Used

- NumPy array manipulation
- Handling missing values
- Broadcasting
- Reshaping arrays
- Concatenation (row-wise and column-wise)
- Axis-based operations
- Statistical analysis (mean, sum, argmax, argmin)
- Data normalization
- Array splitting

---

## Business / Analytical Questions Solved

1. How can missing weather data be handled efficiently?
2. What are the average weather conditions across days?
3. Which day experienced the highest temperature?
4. Which day had the lowest humidity?
5. Which weather feature dominates overall conditions?
6. How does adding new data affect analysis?
7. How can weather data be normalized for comparison?

---

## Learning Outcomes

- Strong understanding of NumPy-based data processing
- Ability to handle incomplete datasets
- Improved understanding of row vs column operations
- Practical knowledge of vectorized operations
- Foundation for real-world data analysis workflows

---

## Tech Stack

- Python
- NumPy

---

## Future Improvements

- Visualization using Matplotlib or Seaborn
- Integration with Pandas for advanced data handling
- Use of real-world weather datasets (CSV files)
- Extension into machine learning preprocessing pipelines

---

## Author

Sarthak Jain

---

## Note

This project is built for learning purposes and demonstrates how NumPy can be used for efficient data analysis and preprocessing in real-world scenarios.

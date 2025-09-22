
# Interview Questions & Answers - Task 1

## 1. What are the different types of missing data?
- **MCAR (Missing Completely at Random):** Missingness is independent of data.
- **MAR (Missing at Random):** Missingness is related to observed data, not the missing value itself.
- **MNAR (Missing Not at Random):** Missingness depends on unobserved/missing data.

## 2. How do you handle categorical variables?
- **Label Encoding:** Assigns numeric values (0, 1, 2, ...) to categories.
- **One-Hot Encoding:** Creates separate binary columns for each category.

## 3. What is the difference between normalization and standardization?
- **Normalization:** Scales data to a fixed range (usually [0, 1]).
- **Standardization:** Rescales data to mean = 0 and standard deviation = 1.

## 4. How do you detect outliers?
- **Boxplot visualization**
- **Interquartile Range (IQR) method**
- **Z-score method**

## 5. Why is preprocessing important in ML?
- Removes noise and inconsistencies
- Improves accuracy and efficiency of models
- Ensures fair feature contribution

## 6. What is one-hot encoding vs label encoding?
- **One-hot encoding:** Creates binary columns, avoids ordinal assumption.
- **Label encoding:** Assigns integers but may introduce false ordinal relationships.

## 7. How do you handle data imbalance?
- **Resampling methods**: Oversampling minority, undersampling majority
- **Synthetic data generation**: SMOTE
- **Use weighted models**

## 8. Can preprocessing affect model accuracy?
- Yes, proper preprocessing improves accuracy, reduces bias, and speeds up training.
- Poor preprocessing can lead to misleading results and underperforming models.

'''
Numpy Arrays for Easy Math and Statistical Functions with Scipy
'''

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

#Creating Arrays
arr = np.array([1, 2, 3, 4, 5])  # Create a one-dimensional array
matrix = np.array([[1, 2, 3], [4, 5, 6]])  # Create a two-dimensional array

print(matrix)

#Array Manipulation
# Reshaping an array
reshaped_matrix = matrix.reshape(3, 2)
print(reshaped_matrix)

# Slicing and indexing
element = matrix[1, 2]
row = matrix[1, :]  # Select the second row
column = matrix[:, 0]  # Select the first column

#Mathematical Operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise addition
result = a + b  # [5, 7, 9]

# Element-wise multiplication
result = a * b  # [4, 10, 18]

# Dot product
dot_product = np.dot(a, b)  # 32

#Linear Algebra
# Matrix multiplication
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
result = np.dot(A, B)

#Descriptive Statistics
data = np.array([12, 15, 18, 21, 24, 27, 30])
mean = np.mean(data)
median = np.median(data)
variance = np.var(data)
std_deviation = np.std(data)

#Random number generation
random_data = np.random.normal(0, 1, size=(3, 3))

# One-sample t-test example
sample_data = np.array([35, 36, 37, 37, 38, 38, 38, 39, 39, 40])
t_stat, p_value = stats.ttest_1samp(sample_data, 37.5)

# Two-sample t-test example
group1 = np.array([24, 25, 26, 27, 28])
group2 = np.array([30, 32, 33, 34, 35])
t_stat, p_value = stats.ttest_ind(group1, group2)

# Calculate means and standard errors
mean_group1 = np.mean(group1)
mean_group2 = np.mean(group2)
sem_group1 = np.std(group1, ddof=1) / np.sqrt(len(group1))
sem_group2 = np.std(group2, ddof=1) / np.sqrt(len(group2))

# Create a bar plot to visualize the means and their standard errors
plt.figure(figsize=(8, 6))
plt.bar(['Group 1', 'Group 2'], [mean_group1, mean_group2], yerr=[sem_group1, sem_group2], capsize=10, color=['b', 'g'])

# Add t-test result to the plot
if p_value < 0.05:
    plt.text(0.5, mean_group1 + 2, 'p < 0.05', fontsize=12, color='r', horizontalalignment='center')
else:
    plt.text(0.5, mean_group1 + 2, 'p = {:.2f}'.format(p_value), fontsize=12, color='b', horizontalalignment='center')

plt.xlabel('Groups')
plt.ylabel('Mean')
plt.title('T-Test Results')
plt.grid(axis='y')

# Show the plot
plt.show()

# Confidence Intervals
data = np.array([85, 89, 92, 88, 94, 97, 91, 82, 100, 96])
confidence_interval = np.percentile(data, [2.5, 97.5])
print(confidence_interval)

# Create a box plot to visualize the data and confidence interval
plt.figure(figsize=(8, 4))
plt.boxplot(data, vert=False, showmeans=True, widths=0.7, patch_artist=True)
plt.axvline(confidence_interval[0], color='r', linestyle='--', label='2.5th Percentile')
plt.axvline(confidence_interval[1], color='b', linestyle='--', label='97.5th Percentile')

plt.xlabel('Value')
plt.title('Box Plot with 95% Confidence Interval')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

df = pd.read_csv('data.csv')

# Extract the biomarker concentration and enzyme activity data
biomarker_concentration = df['Biomarker_Concentration']
enzyme_activity = df['Enzyme_Activity']

# Perform a correlation analysis
correlation, p_value = stats.pearsonr(biomarker_concentration, enzyme_activity)

# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(biomarker_concentration, enzyme_activity)

# Create a scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(biomarker_concentration, enzyme_activity, label='Data Points', color='b')

# Add regression line to the plot
plt.plot(biomarker_concentration, intercept + slope * biomarker_concentration, 'r', label='Regression Line')

# Set titles and labels
plt.title('Biomarker Concentration vs. Enzyme Activity')
plt.xlabel('Biomarker Concentration')
plt.ylabel('Enzyme Activity')
plt.legend()
plt.grid(True)

# Show correlation and regression analysis results
print(f'Correlation: {correlation:.2f}')
print(f'R-squared (Goodness of Fit): {r_value ** 2:.2f}')
print(f'Regression Equation: Enzyme Activity = {intercept:.2f} + {slope:.2f} * Biomarker Concentration')
print(f'p-value: {p_value}')

# Show the plot
plt.show()

data = pd.read_csv('microbiological_data.csv', index_col='Sample')

# Create a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(data, cmap='YlGnBu', annot=True, fmt=".1f", linewidths=0.5)

plt.title('Microbiological Heatmap')
plt.xlabel('Microbial Species')
plt.ylabel('Sample')

# Show the plot
plt.show()
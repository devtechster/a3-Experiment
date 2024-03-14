# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 12:45:41 2024

@author: oz_ge
"""

import numpy as np
from scipy.stats import bootstrap
import matplotlib.pyplot as plt
import pandas as pd
participant_values = np.array([
    [90, 30, 15, 65, 20, 45, 80, 35, 10, 50, 80, 12, 50, 88, 50, 55, 40, 45, 15, 35],
    [85, 25, 10, 66, 20, 25, 66, 33, 5, 95, 50, 8, 66, 60, 33, 50, 30, 33, 12, 30],
    [70, 35, 30, 65, 40, 25, 80, 35, 10, 90, 55, 15, 50, 85, 40, 60, 45, 35, 15, 20],
    [90, 25, 20, 87, 20, 26, 75, 33, 10, 98, 71, 12, 90, 85, 40, 50, 40, 28, 16, 30],
    [80, 30, 20, 60, 25, 30, 65, 30, 10, 90, 60, 10, 95, 70, 45, 60, 45, 33, 20, 75],
    [95, 30, 15, 40, 20, 30, 80, 25, 10, 95, 60, 10, 95, 90, 45, 50, 70, 45, 13, 30],
    [60, 25, 15, 45, 20, 30, 65, 40, 10, 90, 80, 10, 85, 75, 35, 45, 50, 30, 15, 25],
    [90, 40, 30, 70, 33, 30, 75, 40, 15, 95, 95, 12, 85, 80, 45, 50, 50, 50, 20, 40],
    [90, 30, 20, 60, 20, 30, 80, 30, 10, 100, 50, 10, 90, 60, 40, 55, 50, 35, 17, 30],
    [15, 33, 25, 66, 33, 33, 70, 40, 10, 100, 75, 12, 80, 75, 50, 50, 50, 50, 20, 33],
    [80, 30, 15, 50, 20, 34, 70, 30, 10, 95, 75, 8, 90, 80, 40, 65, 40, 33, 15, 30],
    [100, 25, 20, 50, 33, 50, 90, 33, 10, 100, 75, 15, 100, 95, 45, 70, 50, 33, 20, 33],
    [100, 30, 40, 60, 33, 30, 55, 25, 10, 90, 80, 15, 100, 85, 40, 75, 50, 30, 18, 25],
    [90, 30, 20, 75, 20, 33, 65, 45, 15, 90, 85, 15, 80, 70, 40, 70, 55, 40, 20, 25],
    [85, 40, 16, 80, 20, 25, 80, 30, 10, 95, 60, 10, 80, 70, 30, 60, 40, 40, 15, 30],
    [87, 34, 18, 73, 23, 30, 68, 28, 11, 97, 58, 8, 87, 62, 42, 59, 35, 28, 19, 30],
])

true_values = np.array([
    85, 38, 24, 63, 25, 36.67, 68, 38, 10, 91.3, 60, 12.5, 77.8, 66.67, 45.83, 56.67, 42.86, 40, 19, 36
])

# Function to calculate the cm-error
def calculate_cm_error(judged, true):
    return np.log2(np.abs(judged - true) + 1/8)

# Calculate cm-errors for all participants and visualizations
cm_errors = np.array([calculate_cm_error(participant_values[:, i], true_values[i]) for i in range(participant_values.shape[1])]).T
# Calculate the average cm-error for each visualization across all participants
average_errors = cm_errors.mean(axis=0)

# Calculate bootstrapped 95% confidence intervals for each visualization
bootstrapped_cis = [bootstrap((cm_errors[:, i],), np.mean, n_resamples=10000, confidence_level=0.95) for i in range(cm_errors.shape[1])]
ci_lowers = np.array([ci.confidence_interval.low for ci in bootstrapped_cis])
ci_uppers = np.array([ci.confidence_interval.high for ci in bootstrapped_cis])

# Error bar lengths (difference between the mean and the confidence interval bounds)
error_bars = [average_errors - ci_lowers, ci_uppers - average_errors]

# Generate index positions for the y-axis
y_positions = np.arange(len(average_errors))

# Plot error bars for each visualization
plt.errorbar(average_errors, y_positions, xerr=error_bars, fmt='o', color='black', capsize=5)

# Labels and title
plt.ylabel('Visualization Number')
plt.xlabel('Average log2Error')
plt.title('Average log2Error with 95% Bootstrapped Confidence Intervals for Each Visualization')
plt.yticks(y_positions)
# Show grid and plot
plt.grid(True, linestyle='--', linewidth=0.5)
plt.show()

##
indexed_errors = list(enumerate(average_errors))
# Sort by average errors
sorted_indexed_errors = sorted(indexed_errors, key=lambda x: x[1])

# Sort the average errors and the corresponding confidence intervals
sorted_indices = [index for index, error in sorted_indexed_errors]
sorted_average_errors = np.array([error for index, error in sorted_indexed_errors])
sorted_error_bars = [sorted_average_errors - ci_lowers[sorted_indices],
                     ci_uppers[sorted_indices] - sorted_average_errors]

# Generate new y-positions based on the sorted order
sorted_y_positions = np.arange(len(sorted_average_errors))

# Plot error bars for each visualization, sorted from best to worst
plt.errorbar(sorted_average_errors, sorted_y_positions, xerr=sorted_error_bars, fmt='o', color='black', capsize=5)

# Labels and title
plt.ylabel('Visualization Number (Sorted)')
plt.xlabel('Average log2Error')
plt.title('Sorted Average log2Error with 95% Bootstrapped Confidence Intervals')
plt.yticks(sorted_y_positions, labels=[f'Vis. {i+1}' for i in sorted_indices])  # Use the original indices as labels
# Show grid and plot
plt.grid(True, linestyle='--', linewidth=0.5)
plt.gca().invert_yaxis()  # Optionally invert y-axis so that the best (lowest error) is at the top
plt.show()
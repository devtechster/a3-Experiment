# -*- coding: utf-8 -*-
"""
@author: adhiraj
"""

import numpy as np
from scipy.stats import bootstrap
import matplotlib.pyplot as plt
import pandas as pd
participant_values = np.array([
[40, 50, 45, 50, 40, 50, 50, 45, 50, 60, 50, 50, 75, 55, 65, 50, 50, 50, 40],
[50, 50, 50, 50, 50, 50, 50, 45, 50, 60, 50, 50, 45, 55, 65, 50, 60, 60, 45],
[33, 37, 36, 36, 46, 43, 49, 40, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 47],
[50, 50, 50, 30, 40, 25, 50, 25, 50, 60, 40, 50, 40, 50, 50, 50, 30, 30, 50],
[30, 35, 46, 30, 30, 40, 45, 40, 30, 45, 30, 50, 60, 50, 30, 30, 30, 30, 25],
[25, 25, 25, 30, 20, 30, 10, 20, 35, 40, 25, 50, 90, 50, 70, 30, 30, 55, 30],
[40, 70, 60, 30, 70, 20, 20, 58, 50, 50, 50, 65, 80, 51, 60, 60, 50, 50, 60],
[20, 25, 25, 25, 20, 25, 15, 20, 15, 20, 20, 50, 60, 30, 30, 25, 30, 30, 20],
[43, 43, 50, 43, 43, 43, 67, 50, 50, 67, 50, 50, 35, 67, 60, 43, 35, 25, 45],
[35, 50, 30, 70, 30, 60, 50, 60, 70, 50, 60, 100, 60, 40, 30, 30, 30, 40, 30],
[40, 50, 45, 60, 55, 50, 30, 45, 45, 70, 45, 50, 20, 50, 40, 50, 40, 40, 35],
[35, 25, 30, 15, 50, 20, 10, 30, 10, 65, 45, 50, 30, 25, 30, 20, 25, 30, 35],
[30, 30, 25, 35, 35, 35, 20, 30, 15, 25, 15, 25, 35, 40, 60, 20, 25, 55, 30],
[33, 33, 66, 66, 66, 65, 75, 33, 50, 25, 60, 25, 5, 20, 60, 33, 60, 60, 45],
[50, 40, 50, 50, 40, 50, 40, 25, 50, 60, 40, 50, 25, 50, 40, 50, 40, 30, 40],
[50, 50, 50, 40, 50, 40, 50, 50, 50, 70, 50, 50, 90, 50, 60, 50, 50, 80, 60],
[33, 33, 50, 33, 33, 33, 50, 45, 50, 50, 33, 50, 30, 50, 60, 50, 30, 35, 20]

])

true_values = np.array([
    50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50 
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
plt.yticks(sorted_y_positions, labels=[f'Vis. {i+1}' for i in sorted_indices])  # Use the original indices as labels
# Show grid and plot
plt.grid(True, linestyle='--', linewidth=0.5)
plt.gca().invert_yaxis()  # Optionally invert y-axis so that the best (lowest error) is at the top
plt.show()
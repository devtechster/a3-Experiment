# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 20:11:34 2024

@author: oz_ge
"""
import numpy as np
from scipy.stats import bootstrap
import matplotlib.pyplot as plt
import pandas as pd

participant_values_pie = np.array([
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

true_values_pie = np.array([
    85, 38, 24, 63, 25, 36.67, 68, 38, 10, 91.3, 60, 12.5, 77.8, 66.67, 45.83, 56.67, 42.86, 40, 19, 36
])

# Function to calculate the cm-error
def calculate_cm_error(judged, true):
    return np.log2(np.abs(judged - true) + 1/8)
# Calculate cm-error for all participants
errors_pie = np.array([calculate_cm_error(participant, true_values_pie) for participant in participant_values_pie])

# Calculate mean log2Error for each participant
mean_errors_pie = np.mean(errors_pie, axis=1)

# Bootstrap for 95% CI
res_pie = bootstrap((mean_errors_pie,), np.mean, confidence_level=0.95, n_resamples=10000, method='percentile')

df = pd.DataFrame(columns=["Visualization Type", "Mean Error", "Lower Confidence", "Upper Confidence"])
row1 = pd.DataFrame([{"Visualization Type": "Pie Chart", "Mean Error": np.mean(mean_errors_pie), "Lower Confidence": res_pie.confidence_interval[0], "Upper Confidence":  res_pie.confidence_interval[1]}])
####
participant_values_tree = np.array([
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

true_values_tree = np.array([
    50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50 
])

# Calculate cm-error for all participants
errors_tr = np.array([calculate_cm_error(participant, true_values_tree) for participant in participant_values_tree])

# Calculate mean log2Error for each participant
mean_errors_tr = np.mean(errors_tr, axis=1)

# Bootstrap for 95% CI
res_tr = bootstrap((mean_errors_tr,), np.mean, confidence_level=0.95, n_resamples=10000, method='percentile')
row2 = pd.DataFrame([{"Visualization Type": "Tree Map", "Mean Error": np.mean(mean_errors_tr), "Lower Confidence": res_tr.confidence_interval[0], "Upper Confidence":  res_tr.confidence_interval[1]}])
df = pd.concat([df, row1, row2], ignore_index=True)

###



##

# Create a horizontal error bar plot
# Convert the confidence intervals to error margins
error = [
    df["Mean Error"] - np.array(df["Lower Confidence"]),
    np.array(df["Upper Confidence"]) - df["Mean Error"]
]

# Plotting
plt.figure(figsize=(9, 3))
plt.errorbar(df["Mean Error"],df["Visualization Type"], xerr=error, fmt='o', color='black', ecolor='black', capsize=5, elinewidth=2, capthick=2)
plt.title('Mean Error with Confidence Intervals for Different Visualization Types')
plt.show()


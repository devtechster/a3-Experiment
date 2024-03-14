Assignment 3 - Replicating a Classic Experiment  
===
* Experiment 1 link: https://forms.gle/SzZsSXLjd8DFFFNX6
* Experiment 2 link:https://docs.google.com/forms/d/e/1FAIpQLSc5z-g1_s5byEVxiPVpLy9f_laUAA0Z-j0wfilXcFdy5ub1fw/viewform?usp=sf_link
* Experiment 3 link:https://forms.gle/gwP8EfjWpiPHx5rY7

For our experiment, we asked participants to compare **bar charts**, **pie charts**, and **tree maps**. We used Google Forms to host the experiment for the sake of practicability. We have 200 trials for each type of visualization.

Pie Chart
===
<img src= "https://github.com/OzgeAygul/a3-Experiment/assets/77694285/4e33d2fa-6c6f-47cb-8b24-a4451dd5e6a6" alt="image" width="300" height="200">

* The chart above shows log errors of 20 pie charts along with the bootstraped confidence intervals.

* The first thing you might realize is that error bars are not symmetric. When data is not normally distributed, the confidence intervals might naturally be asymmetric. The bootstrap method, which is robust to non-normal distributions, can yield asymmetric confidence intervals that are a more accurate representation of the uncertainty in the estimate.

* There is a great variance between charts, for example, charts 9 (having the most accurate estimations) and 13 (having the worst estimations). You can see all the pie charts in the folder.
  
**Chart 9** 
<img src="https://github.com/OzgeAygul/a3-Experiment/assets/77694285/bc496848-e379-43ba-9690-0a2721d3d2be" alt="image" width="300" height="200">
<img src="https://github.com/OzgeAygul/a3-Experiment/assets/77694285/d1bc3ab7-13f0-4e91-b68f-c557752c6d36" alt="image" width="300" height="200">
**Chart 13**


* The reason that leads to this can be 1) **Position**: When marked slices are adjacent to each other, it could be easier to judge. 2) **Number of data points**: When the number of data points is higher, it may be harder to judge. 3) **Difference**: When there is a significant difference in angles, it is easier to compare.
* For this experiment, the number of slices is randomly generated between 5 and 10, and 2 of them are randomly marked.
* Then participants are asked to compare marked slices.
* After collecting data, accuracy is calculated using the formula below:
  <img src="https://github.com/OzgeAygul/a3-Experiment/assets/77694285/bc0c3c73-f670-40f6-9038-a8edb168cb6b" alt="image">
* Then error bars are bootstrapped with 95% confidence intervals, and sorted from best to worst estimations. 
* Chart 8 seems to perform on average, and can be used to compare with bar chart and tree map.
  

Bar Chart
===
The chart below shows log errors of 20 bar charts.
<img src="https://github.com/devtechster/a3-Experiment/blob/master/BarChart/Bar_Logerror-1.png?raw=true" alt="image" width="300" height="200">

There's also a huge variance between these charts, chart 7 has the best estimations.

**Chart 7** 

<img src="https://github.com/devtechster/a3-Experiment/blob/master/BarChart/barchartoutputs/7(2).jpg" alt="image" width="300" height="200">


Treemaps
===
The chart below shows log errors of 20 treemaps(by 18 users) along with the bootstraped confidence intervals.
<img src="https://github.com/devtechster/a3-Experiment/blob/master/treemaps/log1.png" alt="image" width="300" height="200">
<img src="https://github.com/devtechster/a3-Experiment/blob/master/treemaps/log2.png" alt="image" width="300" height="200">

* The x-axis of the graph shows the average log error, while the y-axis shows the visualization number. Each data point on the graph represents the average log error for a particular visualization, and the error bars represent the 95% confidence interval for that error.

* The title of the graph is "Average log2Error with 95% Bootstrapped Confidence Intervals for Each Visualization".
* The x-axis label is "Average log2Error". The y-axis label is "Visualization Number".
* There are 20 data points in the graph, one for each visualization.
* The error bars for some visualizations are larger than others, indicating that there is more uncertainty in the estimated average log  error for those visualizations.
* Overall, the graph can be used to compare the performance of different visualizations based on their average log error. Visualizations with lower average log errors and smaller error bars are considered to be better performing.

* There is a great variance between charts. You can see all the treemaps output in the folder.



**Technical Achievements:**
===

1. **Random Data Generation:** Implemented a system for generating randomized data for each visualization type, ensuring variability and eliminating bias in the experimental setup.

2. **Random Marking of Data Points:** Developed a feature to randomly mark data points within the generated datasets, enhancing the realism of the experiment and mimicking real-world scenarios.

3. **Error Calculation with Log Error:** Utilized the logarithmic error metric to assess the accuracy of participants' judgments, providing a robust and scalable method for evaluating performance across different visualization types.

4. **Bootstrap Method for Confidence Intervals:** Employed the bootstrap method to compute asymmetric confidence intervals for error estimates, enabling a more accurate representation of uncertainty in the data analysis process.

5. **Sorting and Ranking of Estimations:** Implemented a systematic approach to sort and rank estimations based on error metrics, facilitating comparative analysis and identification of superior visualization techniques.

**Design Achievements:**
===

1. **Simplicity and Clarity:** Prioritized simplicity and clarity in visualization design, ensuring that participants could easily interpret and compare the presented data without unnecessary complexity.

2. **Lean Visualization Approach:** Adopted a lean visualization approach, minimizing visual clutter and extraneous elements to focus participants' attention on the core aspects of the experiment.

3. **Consistent Visual Language:** Maintained consistency in visual language across all visualization types, promoting ease of understanding and reducing cognitive load for participants navigating the experiment.

4. **User-Friendly Interface:** Designed the experiment interface with user-friendliness in mind, optimizing layout and interaction elements to enhance usability and overall participant experience.

5. **Visual Integrity Preservation:** Ensured the preservation of visual integrity in the presentation of data, avoiding distortion or manipulation that could lead to misleading interpretations by participants.

# Trip Planning for Accessibility Analysis with OpenTripPlanner 

For my master thesis I conductedd two seperate trip planning efforts: 
* for a predetermined set of origin-destination pairs, determine travel time with car, public transit and walking. 
* for a predetermined set of origins (centroids of census blocks to be precise) and a set of destinations (the locations of jobs, shops and healthcare facilties to be precise) determine travel time with car, public transit and walking. 

This folder contains the following folders:
* 'graph-build' contains all files required to build a graph with OTP 1.3
* 'compete' contains all files required to calculate the travel time for a predetermined set of origin-destination pairs. 
* 'access' contains all files required to calculate the travel time from a predetermined set of origins to a predetermined set of destinations. 

This code was inspired by/you can find more examples on how to use OTP here: 
* Rafael Pereira: https://github.com/rafapereirabr/otp-travel-time-matrix 
* Jerome Mayaud: https://github.com/jeromemayaud/OpenTripPlanner-OD-matrix 
* Michael Widener/Spatial Analysis of Urban Systems Lab at the University of Toronto: https://github.com/SAUSy-Lab/OpenTripPlanner_analysis 
 
The following steps should be taken when you want to do this... 

I struggled quite a bit with getting OTP to run (smoothly and fast). Here are some tips:

For getting it to work:
* Check your Java version! Both OTP and Jython were only runable on my device if I used version 8 (or 1.8). 

For getting it to work fast:
* I initially planned to evaluate my origin-destinations pairs one by one. This meant that for each origin I would calculate the path to one destintation, store that travel time and move on to the next pair. However, this does not really fit with how OTP works. Due to the way OTP evaluates the graph ones you set the origin, calculating the travel time to several destinations at once costs virtually no time. 

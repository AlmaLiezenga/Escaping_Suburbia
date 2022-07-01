# Code Overview for my master thesis

Late June 2022 I submitted my master thesis 'Escaping Suburbia: A Case Study on Microtransit and Access Equity in the Minneapolis-St.Paul Metropolitan Area' in partial fulfillment of the master degree Engineering & Policy Analysis at TU Delft, The Netherlands. For this thesis I used Python, Jython and Excel quite extensively. I have chosen to not share all my code on GitHub since some if it is privacy-sensitive, boring, and/or not really applicable to any other purposes. But a few segments seemed crucial to share for a combination of transparency reasons and also to help others who might be using the same software. 

This repository contains the following folders: 
* 'Trip_Planning' contains all files required to build a graph with OTP 1.3 Technique for extracting travel times (and in some cases distances) both for access levels and for individual origin-destination pairs, along with an explanation of how to use OpenTripPlanner 1.3 for this purpose. 
* 'Accessibility_Analysis' contains scripts that convert the .csv output of the trip planning efforts to cumulative accessibility scores and contains a dummy Excel file showing how you can create a Lorenz curve and Gini coefficient from that data. 

If you have specific questions about the code and how to implement it feel free to drop me a question/open an issue, always willing to help out and/or provide clarity. The full thesis pdf can be found here: https://repository.tudelft.nl/islandora/object/uuid:aa717089-f319-4e76-928f-6bec4e141e49?collection=education 

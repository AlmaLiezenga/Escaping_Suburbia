#!/usr/bin/jython
from org.opentripplanner.scripting.api import OtpsEntryPoint

# Instantiate an OtpsEntryPoint
otp = OtpsEntryPoint.fromArgs(['--graphs', '.',
                               '--router', 'graph_folder'])

# Start timing the code
import time
start_time = time.time()

# Get the default router
router = otp.getRouter('graph_folder')

# Create a default request for a given departure time
req = otp.createRequest()
# define transport mode
req.setModes('WALK')     
#req.setMaxTimeSec(3600) 

origins = otp.loadCSVPopulation('origins_B_2.csv', 'latitude', 'longitude')
destinations = otp.loadCSVPopulation('destinations_B.csv', 'latitude', 'longitude')

# Create a CSV output
matrixCsv = otp.createCSVOutput()
matrixCsv.setHeader(['GEO_ID_origin', 'GEO_ID_destination', 'Walk: Walking Distance (meters)', 'Walk: Total Travel Time (seconds)'])

#Read Points of Origin and Destination - The files contain the columns GEOID, X [longitude], Y [latitude] and HourOfDay
#combine into one document and directly iterative over rows with for loop
for origin in origins: 
    print(time.time())
    req.setOrigin(origin)

    shortest_path_tree = router.plan(req)

    if shortest_path_tree is None: continue

    evaluated = shortest_path_tree.eval(destinations)
    print(time.time())

    for r in evaluated: 
        matrixCsv.addRow([ origin.getStringData('GEO_ID'), r.getIndividual().getStringData('GEO_ID'), r.getWalkDistance() , r.getTime()])
    
    print(time.time())
    print('completed run for', origin.getStringData('GEO_ID'))

# Save the result
matrixCsv.save('traveltimes/traveltimes_walk_B_2.csv')

# Stop timing the code
print("Elapsed time was %g seconds" % (time.time() - start_time))

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

origins = otp.loadCSVPopulation('origins/origins.csv', 'latitude', 'longitude')
destinations = otp.loadCSVPopulation('destinations/jobs_destinations.csv', 'LATITUDE', 'LONGITUDE')

# Create a CSV output
matrixCsv = otp.createCSVOutput()
matrixCsv.setHeader(['GEO_ID_origin', 'TRACTCE_destinations', 'BLKGRPCE_destination', 'Number of jobs', 'Transit: Walking Distance (meters)', 'Transit: Total Travel Time (seconds)', 'Transit: Boardings'])

#Read Points of Origin and Destination - The files contain the columns GEOID, X [longitude], Y [latitude] and HourOfDay
#combine into one document and directly iterative over rows with for loop
for origin in origins:

    # Create a default request for a given departure time
    req = otp.createRequest()
    # define transport mode
    req.setModes('TRANSIT, BUS, RAIL, SUBWAY, TRAM, WALK')     
    req.setMaxTimeSec(10800) 
 
    print(time.time())
    req.setOrigin(origin)

    shortest_path_tree = router.plan(req)

    if shortest_path_tree is None: continue

    evaluated = shortest_path_tree.eval(destinations)
    print(time.time())

    for r in evaluated: 
        matrixCsv.addRow([ origin.getStringData('GEOID20'), r.getIndividual().getStringData('TRACTCE'), r.getIndividual().getStringData('BLKGRPCE'), r.getIndividual().getStringData('C000'),  r.getWalkDistance() , r.getTime(), r.getBoardings()])
    
    print(time.time())
    print('completed run for', origin.getStringData('GEOID20'))

# Save the result
matrixCsv.save('traveltimes/traveltimes_jobs_transit.csv')

# Stop timing the code
print("Elapsed time was %g seconds" % (time.time() - start_time))

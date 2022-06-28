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
req.setModes('TRANSIT, BUS, RAIL, SUBWAY, TRAM, WALK')     
#req.setMaxTimeSec(3600) 

origins = otp.loadCSVPopulation('pt_origins_B_2022_4.csv', 'origin latitude', 'origin longitude')
destinations = otp.loadCSVPopulation('pt_destinations_B_2022.csv', 'destination latitude', 'destination longitude')

# Create a CSV output
matrixCsv = otp.createCSVOutput()
matrixCsv.setHeader(['GEO_ID_origin', 'GEO_ID_destination', 'Year', 'Month', 'Day', 'Hour', 'Transit: Walking Distance (meters)', 'Transit: Total Travel Time (seconds)', 'Transit: Number of Boardings'])

#Read Points of Origin and Destination - The files contain the columns GEOID, X [longitude], Y [latitude] and HourOfDay
#combine into one document and directly iterative over rows with for loop
for origin in origins: 
    print(time.time())
    year = int(origin.getStringData('date_year'))
    month = int(origin.getStringData('date_month'))
    day = int(origin.getStringData('date_day'))
    hour = int(origin.getStringData('time_hour'))
    req.setDateTime(year, month, day, hour, 30, 00)  # set departure time

    req.setOrigin(origin)

    shortest_path_tree = router.plan(req)

    if shortest_path_tree is None: continue

    evaluated = shortest_path_tree.eval(destinations)
    print(time.time())

    for r in evaluated: 
        matrixCsv.addRow([ origin.getStringData('GEO_ID_origin'), r.getIndividual().getStringData('GEO_ID_destination'), year, month, day, hour, r.getWalkDistance() , r.getTime(), r.getBoardings()])
    
    print(time.time())
    print('completed run for', origin.getStringData('GEO_ID_origin'))

# Save the result
matrixCsv.save('traveltimes/traveltimes_pt_B_2022_4.csv')

# Stop timing the code
print("Elapsed time was %g seconds" % (time.time() - start_time))
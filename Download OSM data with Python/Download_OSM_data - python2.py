# author: Bartosz Mazurkiewicz
# Downloading OSM data via the overpass API. Pay attention to not generate that much traffic.
# The servers are for everyone and the resources are limited. See the usage policy at http://wiki.openstreetmap.org/wiki/Overpass_API

import time
import os
import urllib

# Bounding box - example Florence, Italy
north = str(43.8)
south = str(43.75)
east = str(11.3)
west = str(11.2)
              
# bbox=west,south,east,north
url = 'http://www.overpass-api.de/api/map?bbox=' + west +',' + south + ',' + east + ',' + north
       
# Download osm data and print download time
start = time.time()
       
urllib.urlretrieve(url, 'DataOSM.osm')
       
end = time.time()
print("Download OSM data took " + str(end-start) + " seconds")
print("Data size is about " + str(os.path.getsize(os.getcwd() + "\\DataOSM.osm")/1000000) + " mb")

from geopy.geocoders import GoogleV3
from geopy.exc import GeocoderTimedOut
import time    # For rate limiting purposes

# Using Geopy copyright 2006-2016 geopy authors
# Geopy available at https://github.com/geopy/geopy

# This program is copyright 2017 Joseph Johaneman
# And is released under the MIT License

# What this does:  this program reads in a list of addresses of
# school names and prints out a tab separated list of schools name
# latitude and longitude.  Obviously, this can be redirected to
# a text file by redirecting standard output

# Create the Google Maps API Object.  Note you need an API Key
googleLocator=GoogleV3(api_key='<Your Google Map Geoencode API Key>')

# First we need the list of schools
filename="SchoolList.txt"

# Create a list to score the School Names loaded them from a file
with open(filename) as f:
    schools=f.read().splitlines()
# print header
print "School Name\tLatitude\tLongitude"

# Loop through the school names and get locations
for i in schools:
    try:  #Exception handling is important!
        location=googleLocator.geocode(i, exactly_one=True)
    except GeocoderTimedOut: # in case we time out:
         print i, "\t0\t-1"  # print 0, -1.  We'll check for it later
    else:  # Okay we didn't time out
        if location != None:   # if we find something
            print i, "\t", location.latitude, "\t", location.longitude #print it
        else:  # Didn't find it.  Print zeroes
            print i, "\t0\t0"  # otherwise print 0s.  We'll check for it later
        time.sleep(.3)  # This waits 300 milliseconds between requests to be nice

# Note:  I chose to print 0, -1 for timeouts and 0, 0 for not found so I'd know
# how many exceptions were thrown.

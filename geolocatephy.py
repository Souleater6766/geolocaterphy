import geocoder
import os

# Create folder to store location data
if not os.path.exists('location_data'):
    os.makedirs('location_data')

# Get location and save to file
g = geocoder.ip('me')
with open('location_data/location.txt', 'w') as f:
    f.write(str(g.latlng))

# Confirm that the location was saved
with open('location_data/location.txt', 'r') as f:
    location = f.read()
print(f'Location saved: {location}')

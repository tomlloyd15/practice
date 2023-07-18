from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="tobywilkins1@gmail.com")
location = geolocator.geocode("Red House, sheen lane, london")
print(location.address)
#Flatiron Building, 175, 5th Avenue, Flatiron, New York, NYC, New York, ...
print((location.latitude, location.longitude))
print(location.raw)
#{'place_id': '9167009604', 'type': 'attraction', ...}

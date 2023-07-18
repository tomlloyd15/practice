"""
import folium

def plot_point_on_map(latitude, longitude):
    map = folium.Map(location=[latitude, longitude], zoom_start=15)
    folium.Marker([latitude, longitude]).add_to(map)
    return map

# Example usage
latitude = 51.4602295
longitude = -0.26809601031831837
map = plot_point_on_map(latitude, longitude)
map.save("map.html")
map.save("map.png")
print("Map saved as map.png.")
"""

import folium
from geopy.geocoders import Nominatim

def plot_location_on_map(address):
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.geocode(address)
    
    if location:
        map = folium.Map(location=[location.latitude, location.longitude], zoom_start=15)
        
        # Add an arrow marker
        folium.Marker(
            location=[location.latitude, location.longitude],
            icon=folium.Icon(icon='arrow-up', prefix='fa', color='red'),
            popup=folium.Popup(address, max_width=250),
        ).add_to(map)
        
        map.save("map.html")
        print(f"Map saved as 'map.html' with arrow pointing at '{address}'.")
    else:
        print("Address not found.")

if __name__ == "__main__":
    address = input("Enter an address: ")
    plot_location_on_map(address)

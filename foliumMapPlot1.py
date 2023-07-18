
import folium
import io

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


from PIL import Image

img_data = map._to_png(5)
img = Image.open(io.BytesIO(img_data))
img.save('image.png')


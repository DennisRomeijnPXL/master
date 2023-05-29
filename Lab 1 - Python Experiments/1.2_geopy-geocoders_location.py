from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="specify_your_app_name_here")

location = geolocator.reverse("52.509669, 13.376294")
## print location of previous mentioned coordinates
print(location.address)
## print coordinates
print((location.latitude, location.longitude))
## show the response of geopy
print(location.raw)

from geopy.geocoders import Nominatim
## use website
geolocator = Nominatim(user_agent="http://biasc.be")
city_country = "Brussels, Belgium"
##locate the previous mentioned city
location = geolocator.geocode(city_country)
## prints location
print(location.address)
devnet_lat = location.latitude
devnet_lon = location.longitude
## prints coordinates
print((devnet_lat, devnet_lon))

# from geopy.geocoders import Nominatim
import geocoder

def getPosition():
    location = '東京タワー'
    ret = geocoder.osm(location, timeout=5.0)
    print(ret.latlng)
    print(ret.address)


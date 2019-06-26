import requests
from geopy.geocoders import Nominatim


latitude = '0.3324567'
longitude = '32.123467'

latlng = latitude + ',' + longitude

# Enter your api key here 
api_key = "AIzaSyAH6Tx3JJQvAkt4Tbw3tBWiSO8bLFrN41w" 

#AIzaSyASmoLdB8WBkLBy0Wob9yAtuSqlPEq5D28

  
# url variable store url 
url = "https://maps.googleapis.com/maps/api/staticmap?"
  
# center defines the center of the map, 
# equidistant from all edges of the map. 
latfloat = float(latitude)
longfloat = float(longitude)
            
latlng = latitude + ',' + longitude
geolocator = Nominatim(user_agent='gpslocator')
location = geolocator.reverse(latlng)

location_string  = str(location)


print(location_string.split(",")[0])

center = location_string.split(",")[0]

  
# zoom defines the zoom 
# level of the map 
zoom = 12
  
# get method of requests module 
# return response object 
r = requests.get(url + "center =" + center + "&zoom =" +
                   str(zoom) + "&size = 400x400&key =" +
                             api_key + "sensor = false") 
  
# wb mode is stand for write binary mode 
f = open('map.png ', 'wb') 
  
# r.content gives content, 
# in this case gives image 
f.write(r.content) 
  
# close mthod of file object 
# save and close the file 
f.close() 



f
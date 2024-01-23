from geopy.geocoders import Nominatim
from shapely import wkb

def get_location_from_address(address):
    geolocator = Nominatim(user_agent="staskrz")
    location = geolocator.geocode(address,exactly_one=True)
    try:
        return location.latitude, location.longitude
    except AttributeError:
        print(f"Nie znaleziono lokalizacji dla adresu: {address}")
        return 52.2296756, 21.0122287
        
def get_address_from_location(lat, lon):
    geolocator = Nominatim(user_agent="staskrz")
    location = geolocator.reverse(f"{lat}, {lon}", exactly_one=True,addressdetails=True,language=["pl","en"])
    if location is None:
        return "Nie znaleziono adresu"
    return location.address

def parse_address(address):
    print(address)
    if address == "Nie znaleziono adresu":
        return "Nie znaleziono adresu"
    address = address.split(',')
    if len(address) ==10:
        street = address[1]
        street_number = address[0]
        city = address[4]
        postal_code = address[8]    
    elif len(address) == 9:
        street = address[1]
        street_number = address[0]
        city = address[4]
        postal_code = address[7]
    elif len(address) == 8:
        street = address[1]
        street_number = address[0]
        city = address[4]
        postal_code = address[6]
    elif len(address) == 3:
        street = address[0]
        street_number = address[1]
        city = address[2]
        postal_code = ""
    elif len(address) == 4:
        street = address[0]
        street_number = address[1]
        city = address[2]
        postal_code = address[3]
    else: return "Nie znaleziono adresu"
    return street.strip(), street_number.strip(), postal_code.strip(), city.strip()

def get_point_from_address(address):
    lat, lon = get_location_from_address(address)
    return f"POINT({lon} {lat})"

def get_lat_lon(wkb_point):
    point = wkb.loads(str(wkb_point), hex=True)
    return (point.y, point.x)
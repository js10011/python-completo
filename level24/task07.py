import requests

def get_coordinates(address, api_key):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": api_key
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            location = data['results'][0]['geometry']['location']
            return location['lat'], location['lng']
        else:
            print(f"Error: {data['status']}")
    else:
        print(f"Failed to connect to the API, status code: {response.status_code}")

# Substitua 'YOUR_API_KEY' pela sua chave real da API do Google Maps
API_KEY = 'YOUR_API_KEY'
address = "1600 Amphitheatre Parkway, Mountain View, CA"
latitude, longitude = get_coordinates(address, API_KEY)
print(f"Coordinates for '{address}': Latitude = {latitude}, Longitude = {longitude}")
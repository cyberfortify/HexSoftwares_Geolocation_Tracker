import requests
import folium
import re


def is_valid_ip(ip):
    """
    Check if the provided IP address is in a valid format.
    Returns True if valid, otherwise False.
    """
    # Regular expression to match valid IP address formats
    ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return ip_pattern.match(ip) is not None


def fetch_geolocation(ip=None):
    """
    Fetch the geolocation data for the given IP address.
    If no IP address is provided, it will use the current IP.
    Returns latitude, longitude, city, region, and country.
    """
    try:
        # Identify the request URL based on whether an IP address is provided
        if ip:
            url = f'https://ipinfo.io/{ip}/json'
        else:
            url = 'https://ipinfo.io/json'

        # Make the API request to fetch geolocation data
        response = requests.get(url)

        # Check if the response is successful
        response.raise_for_status()

        # Parse the JSON data returned by the API
        data = response.json()

        # Extract latitude and longitude from the location data
        if 'loc' in data:
            location = data['loc'].split(',')
            latitude = float(location[0])
            longitude = float(location[1])
        else:
            print("Hmm, it looks like location data is not available.")
            return None, None, None, None, None

        # Extract city, region, and country from the data, defaulting to 'Unknown' if not found
        city = data.get('city', 'Unknown')
        region = data.get('region', 'Unknown')
        country = data.get('country', 'Unknown')

        return latitude, longitude, city, region, country
    except requests.exceptions.RequestException as error:
        print(f"Oops! There was an error fetching data: {error}")
        return None, None, None, None, None


def create_map(lat, lon, city, region, country):
    """
    Create and save a map centered at the given latitude and longitude.
    A marker will indicate the location with city, region, and country information.
    """
    # Create a Folium map centered at the user's location
    user_map = folium.Map(location=[lat, lon],
                          zoom_start=12, tiles='OpenStreetMap')

    # Add a marker on the map with the location information
    folium.Marker(
        [lat, lon],
        # Information displayed on marker click
        popup=f"Location: {city}, {region}, {country}",
        icon=folium.Icon(color='blue', icon='info-sign')  # Blue marker icon
    ).add_to(user_map)

    # Save the map to an HTML file
    user_map.save("user_location.html")
    print("Your location has been created and saved as 'user_location.html'!")


if __name__ == "__main__":
    ip_address = input(
        "Enter an IP address (or leave blank to use your current IP): ")

    # Validate the input IP address format
    if ip_address and not is_valid_ip(ip_address):
        print("That doesn't seem to be a valid IP address. Please try again.")
    else:
        # Fetch geolocation data based on the IP address provided
        latitude, longitude, city, region, country = fetch_geolocation(
            ip_address)

        # Check if the location data was retrieved successfully
        if latitude is not None and longitude is not None:
            create_map(latitude, longitude, city, region, country)
            print(f"Successfully retrieved location: {
                  city}, {region}, {country}.")
        else:
            print("Sorry, we couldn't fetch the location data.")

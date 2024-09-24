# Geolocation Tracker

## Overview

This repository contains the code for the **Geolocation Tracker**, a Python application that fetches the geolocation data of a given IP address. If no IP address is provided, it retrieves the geolocation data for the current user's IP.

## Description

- **Task:** Develop a geolocation tracker that uses the IP address to determine the geographical location of a user.
- **Objective:** To create a simple tool that displays the geographical location (latitude, longitude, city, region, and country) on a map using Folium.
- **Technologies Used:** Python, requests, folium, regex

## Features

- Validate the format of an IP address.
- Fetch geolocation data using the `ipinfo.io` API.
- Create an interactive map using Folium that marks the user's location with city, region, and country information.
- Save the generated map as an HTML file.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/cyberfortify/HexSoftwares_Geolocation_Tracker/
   ```
2. Navigate to the project directory:
   ```bash
   cd HexSoftwares_Geolocation_Tracker/
   ```
3. Install the required packages:
   ```bash
   pip install requests folium
   ```

## Usage

1. Run the Python script:
   ```bash
   python geolocation_tracker.py
   ```
2. When prompted, enter an IP address or leave it blank to use your current IP. The application will retrieve the geolocation data and create a map.

## Output

- The generated map will be saved as `user_location.html` in the project directory. You can open this file in a web browser to view your location on the map.

## Contribution

Feel free to fork this repository and make your own contributions. For any issues or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


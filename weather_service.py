import requests 

def getWeather(city, self):
    """Fetches weather data from the API and updates the UI."""
    api_key = "enter_api_key_here"  # Replace with your actual API key
    city = self.city_input.text()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for invalid responses
        data = response.json()
        
        if response.status_code == 200:
            self.displayWeather(data)
        else:
            print(f"Error fetching weather data: {response.status_code}")
            self.handleHTTPError(response)
    
    except requests.exceptions.HTTPError as http_error:
        self.handleHTTPError(response, http_error)
    except Exception as error:
        print(f"An error occurred: {error}")

def handleHTTPError(self, response, http_error):
    """Handles HTTP errors."""
    print(f"HTTP error occurred: {http_error}")
    print(f"Error response: {response.status_code}")
    if response.status_code == 404:
        self.description_label.setText("City not found.")
    else:
        self.description_label.setText("Unable to fetch weather data.")

import requests

def getWeather(city, app_instance):
    """Fetches weather data from the API and updates the UI."""
    apiKey = "your_api_key_here"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data["cod"] == 200:
            app_instance.displayWeather(data)  # Pass the app instance to update the UI
        else:
            displayError("Unexpected response code: {data['cod']}", app_instance)
        
    except requests.exceptions.HTTPError as http_error:
        handleHTTPError(response.status_code, http_error, app_instance)
    except requests.exceptions.RequestException as req_error:
        displayError(f"Request Error: {req_error}", app_instance)

def handleHTTPError(status_code, error, app_instance):
    """Handles different HTTP errors based on the status code."""
    error_messages = {
        400: "400 Bad Request: Please check your input",
        401: "401 Unauthorized: Invalid API key",
        403: "403 Forbidden: Access denied",
        404: "404 Not Found: City not found",
        500: "500 Internal Server Error: Please try again later",
        502: "502 Bad Gateway: Invalid response from server",
        503: "503 Service Unavailable: Server is down",
        504: "504 Gateway Timeout: Server unresponsive"
    }
    
    message = error_messages.get(status_code, f"HTTP error occurred: {error}")
    displayError(message, app_instance)
    
def displayError(message, app_instance):
    """Displays an error message in the description label."""
    app_instance.description_label.setText(message)

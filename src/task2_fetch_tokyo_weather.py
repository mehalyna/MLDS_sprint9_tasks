import requests
import json


def fetch_weather_data():
    """
    Fetch the maximum temperature forecast for Tokyo using the Open-Meteo API.

    Returns:
        dict: A dictionary containing the date and the maximum temperature.
    """
    url = "https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&daily=temperature_2m_max" \
          "&timezone=Asia/Tokyo"
    response = requests.get(url)
    response.raise_for_status()  # Check that the request was successful

    # Parse the JSON response
    data = response.json()

    # Extract the date and maximum temperature
    date = data['daily']['time'][0]
    max_temperature = data['daily']['temperature_2m_max'][0]

    return {"date": date, "max_temperature": max_temperature}


def save_to_json(data, filename):
    """
    Save the extracted weather data to a JSON file.

    Args:
        data (dict): The data to be saved.
        filename (str): The name of the JSON file.
    """
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    # Fetch the weather data
    weather_data = fetch_weather_data()

    # Save the data to a JSON file
    save_to_json(weather_data, "tokyo_weather.json")

    print("Data successfully saved to tokyo_weather.json")

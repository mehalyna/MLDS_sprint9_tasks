import json
import csv


def load_json(filename):
    """
    Load JSON data from a file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        dict: The loaded JSON data.
    """
    with open(filename, 'r') as f:
        data = json.load(f)
    return data


def summarize_weather_data(data):
    """
    Summarize the weather data across all days.

    Args:
        data (list of dict): The daily weather data.

    Returns:
        dict: A summary of the key metrics across all days.
    """
    total_max_temp = 0
    total_min_temp = 0
    total_precipitation = 0
    total_wind_speed = 0
    total_humidity = 0
    hot_days = 0
    windy_days = 0
    rainy_days = 0
    count = len(data)

    for day in data:
        total_max_temp += day["max_temperature"]
        total_min_temp += day["min_temperature"]
        total_precipitation += day["precipitation"]
        total_wind_speed += day["wind_speed"]
        total_humidity += day["humidity"]

        if day["max_temperature"] > 30:
            hot_days += 1
        if day["wind_speed"] > 15:
            windy_days += 1
        if day["precipitation"] > 0:
            rainy_days += 1

    summary = {
        "average_max_temp": total_max_temp / count,
        "average_min_temp": total_min_temp / count,
        "total_precipitation": total_precipitation,
        "average_wind_speed": total_wind_speed / count,
        "average_humidity": total_humidity / count,
        "hot_days": hot_days,
        "windy_days": windy_days,
        "rainy_days": rainy_days
    }

    return summary


def export_to_csv(data, file):
    """
    Export the summarized weather data to a CSV file or file-like object.

    Args:
        data (list of dict): The daily weather data to export.
        file (str or file-like object): The name of the CSV file to save the data in, or a file-like object.
    """
    headers = ["Date", "Max Temperature", "Min Temperature", "Precipitation", "Wind Speed", "Humidity", "Weather Description", "Is Hot Day", "Is Windy Day", "Is Rainy Day"]

    # Check if 'file' is a string (filename), then open it
    if isinstance(file, str):
        with open(file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            for day in data:
                writer.writerow({
                    "Date": day["date"],
                    "Max Temperature": day["max_temperature"],
                    "Min Temperature": day["min_temperature"],
                    "Precipitation": day["precipitation"],
                    "Wind Speed": day["wind_speed"],
                    "Humidity": day["humidity"],
                    "Weather Description": day["weather_description"],
                    "Is Hot Day": day["max_temperature"] > 30,
                    "Is Windy Day": day["wind_speed"] > 15,
                    "Is Rainy Day": day["precipitation"] > 0
                })
    else:
        # Assume 'file' is a file-like object
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for day in data:
            writer.writerow({
                "Date": day["date"],
                "Max Temperature": day["max_temperature"],
                "Min Temperature": day["min_temperature"],
                "Precipitation": day["precipitation"],
                "Wind Speed": day["wind_speed"],
                "Humidity": day["humidity"],
                "Weather Description": day["weather_description"],
                "Is Hot Day": day["max_temperature"] > 30,
                "Is Windy Day": day["wind_speed"] > 15,
                "Is Rainy Day": day["precipitation"] > 0
            })


if __name__ == "__main__":
    # Load the JSON data
    weather_data = load_json("tokyo_weather_complex.json")

    # Summarize the weather data
    summary = summarize_weather_data(weather_data['daily'])

    # Print the summary for verification
    print("Weather Data Summary:")
    for key, value in summary.items():
        print(f"{key}: {value}")

    # Export the summarized data to a CSV file
    export_to_csv(weather_data['daily'], "tokyo_weather_summary.csv")

    print("Data successfully exported to tokyo_weather_summary.csv")

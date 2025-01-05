import json


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


def analyze_daily_weather(day, temp_threshold=30, wind_threshold=15, humidity_threshold=70):
    """
    Analyze weather data for a single day.

    Args:
        day (dict): The weather data for the day.
        temp_threshold (float): The temperature threshold to determine a hot day.
        wind_threshold (float): The wind speed threshold to determine a windy day.
        humidity_threshold (float): The humidity threshold to determine uncomfortable weather.

    Returns:
        dict: A dictionary with analysis results for the day.
    """
    date = day["date"]
    max_temperature = day["max_temperature"]
    min_temperature = day["min_temperature"]
    precipitation = day["precipitation"]
    wind_speed = day["wind_speed"]
    humidity = day["humidity"]
    weather_description = day["weather_description"]

    is_hot_day = max_temperature > temp_threshold
    temperature_swing = max_temperature - min_temperature
    is_windy_day = wind_speed > wind_threshold
    is_uncomfortable_day = humidity > humidity_threshold
    is_rainy_day = precipitation > 0

    analysis = {
        "date": date,
        "is_hot_day": is_hot_day,
        "temperature_swing": temperature_swing,
        "is_windy_day": is_windy_day,
        "is_uncomfortable_day": is_uncomfortable_day,
        "is_rainy_day": is_rainy_day,
        "weather_description": weather_description
    }

    return analysis


def generate_daily_report(analysis):
    """
    Generate a detailed report based on the analysis results for a single day.

    Args:
        analysis (dict): The analysis results for the day.

    Returns:
        str: A detailed report as a string.
    """
    report = f"Date: {analysis['date']}\n"
    report += f"Weather: {analysis['weather_description']}\n"
    report += f"Temperature: Max {analysis['temperature_swing']}°C\n"
    if analysis["is_hot_day"]:
        report += "It was a hot day.\n"
    if analysis["temperature_swing"] > 10:
        report += f"The temperature swing was significant at {analysis['temperature_swing']}°C.\n"
    if analysis["is_windy_day"]:
        report += "It was a windy day.\n"
    if analysis["is_uncomfortable_day"]:
        report += "The humidity made the day uncomfortable.\n"
    if analysis["is_rainy_day"]:
        report += "It was a rainy day.\n"
    else:
        report += "There was no precipitation.\n"

    return report



def summarize_weather_analysis(analyses):
    """
    Summarize the weather analysis over multiple days.

    Args:
        analyses (list of dict): A list of daily analysis results.

    Returns:
        str: A summary report as a string.
    """
    hottest_day = max(analyses, key=lambda x: x['temperature_swing'])
    windiest_day = max(analyses, key=lambda x: x['is_windy_day'])
    most_humid_day = max(analyses, key=lambda x: x['is_uncomfortable_day'])
    rainiest_day = max(analyses, key=lambda x: x['is_rainy_day'])

    summary = "Weather Summary:\n"
    summary += f"Hottest day: {hottest_day['date']} with a maximum temperature of {hottest_day['temperature_swing']}°C\n"
    summary += f"Windiest day: {windiest_day['date']} with wind speeds of {windiest_day['is_windy_day']} km/h\n"
    summary += f"Most humid day: {most_humid_day['date']} with a humidity level of {most_humid_day['is_uncomfortable_day']}%\n"
    summary += f"Rainiest day: {rainiest_day['date']} with {rainiest_day['is_rainy_day']} mm of precipitation\n"

    return summary


if __name__ == "__main__":
    # Load the JSON data
    weather_data = load_json("tokyo_weather_complex.json")

    # Analyze the weather data for each day
    analyses = [analyze_daily_weather(day) for day in weather_data['daily']]

    # Generate and print daily reports
    for analysis in analyses:
        report = generate_daily_report(analysis)
        print(report)

    # Generate and print a summary report
    summary_report = summarize_weather_analysis(analyses)
    print(summary_report)

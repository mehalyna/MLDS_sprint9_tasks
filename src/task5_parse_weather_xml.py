import xml.etree.ElementTree as ET
import csv


def parse_weather_xml(xml_file):
    """
    Parse weather data from an XML file.

    Args:
        xml_file (str): Path to the XML file.

    Returns:
        list of dict: A list of dictionaries with parsed weather data.
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()

    parsed_data = []
    for day in root.findall('day'):
        date = day.find('date').text
        temperature = day.find('temperature').text
        humidity = day.find('humidity').text
        precipitation = day.find('precipitation').text

        parsed_data.append({
            "date": date,
            "temperature": float(temperature),
            "humidity": int(humidity),
            "precipitation": float(precipitation)
        })

    return parsed_data


def save_to_csv(data, filename="parsed_weather_data.csv"):
    """
    Save parsed weather data to a CSV file.

    Args:
        data (list of dict): Parsed weather data.
        filename (str): Name of the CSV file.
    """
    headers = ["Date", "Temperature", "Humidity", "Precipitation"]
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for entry in data:
            writer.writerow({
                "Date": entry["date"],
                "Temperature": entry["temperature"],
                "Humidity": entry["humidity"],
                "Precipitation": entry["precipitation"]
            })


if __name__ == "__main__":
    # Parse the XML file
    weather_data = parse_weather_xml("weather_data.xml")

    # Save the parsed data to a CSV file
    save_to_csv(weather_data)
    print("Data has been successfully parsed and saved to parsed_weather_data.csv.")

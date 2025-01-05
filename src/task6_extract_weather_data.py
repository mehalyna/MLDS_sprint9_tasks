import csv
import re


def clean_text(line):
    """
    Clean the text line by removing non-ASCII characters and fixing known issues.

    Args:
        line (str): The line of text to clean.

    Returns:
        str: The cleaned line of text.
    """
    # Replace non-breaking spaces and other non-ASCII characters
    line = line.replace("Â", "")
    return line


def extract_weather_data(text_file):
    """
    Extract weather data from a text file using regular expressions.

    Args:
        text_file (str): Path to the text file.

    Returns:
        list of dict: A list of dictionaries with extracted weather data.
    """
    with open(text_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    pattern = r"Date: (\d{4}-\d{2}-\d{2}), Max Temp: ([\d.]+)°C, Min Temp: ([\d.]+)°C, Humidity: (\d+)%?, Precipitation: ([\d.]+)mm"

    extracted_data = []
    for line in lines:
        cleaned_line = clean_text(line)  # Clean the line before processing
        match = re.search(pattern, cleaned_line)
        if match:
            date, max_temp, min_temp, humidity, precipitation = match.groups()
            extracted_data.append({
                "date": date,
                "max_temperature": float(max_temp),
                "min_temperature": float(min_temp),
                "humidity": int(humidity),
                "precipitation": float(precipitation)
            })
        else:
            print(f"No match found for line: {line.strip()}")  # Debugging line

    return extracted_data

def save_to_csv(data, filename="extracted_weather_data.csv"):
    """
    Save extracted weather data to a CSV file.

    Args:
        data (list of dict): Extracted weather data.
        filename (str): Name of the CSV file.
    """
    headers = ["Date", "Max Temperature", "Min Temperature", "Humidity", "Precipitation"]
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for entry in data:
            writer.writerow({
                "Date": entry["date"],
                "Max Temperature": entry["max_temperature"],
                "Min Temperature": entry["min_temperature"],
                "Humidity": entry["humidity"],
                "Precipitation": entry["precipitation"]
            })


if __name__ == "__main__":
    # Extract data from the text file
    weather_data = extract_weather_data("weather_report.txt")

    # Save the extracted data to a CSV file
    save_to_csv(weather_data)
    print("Data has been successfully extracted and saved to extracted_weather_data.csv.")

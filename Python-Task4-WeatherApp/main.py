
import requests
from config import API_KEY

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather():
    print("\n================================")
    print("       WEATHER APPLICATION")
    print("================================")

    location = input(
        "Enter city name or ZIP code: "
    ).strip()

    # Validate input
    if not location:
        print("Error: City name cannot be empty!")
        return

    # Prepare API parameters
    params = {
        "appid": API_KEY,
        "units": "metric"
    }

    # Decide whether input is a ZIP code or city
    if location.replace(" ", "").isdigit():
        params["zip"] = f"{location},IN"
    else:
        params["q"] = location

    try:
        print("\nFetching weather information...")

        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10
        )

        # Handle API errors
        if response.status_code == 404:
            print("Error: City not found!")
            return

        elif response.status_code == 401:
            print("Error: Invalid or inactive API key!")
            return

        elif response.status_code == 429:
            print("Error: API request limit reached!")
            return

        response.raise_for_status()

        # Convert JSON response into Python data
        data = response.json()

        # Extract weather information
        city = data["name"]
        country = data["sys"]["country"]

        temp_c = data["main"]["temp"]
        temp_f = (temp_c * 9 / 5) + 32

        humidity = data["main"]["humidity"]

        condition = data["weather"][0]["description"]

        wind_speed = data["wind"]["speed"]

        # Display results
        print("\n================================")
        print("         WEATHER REPORT")
        print("================================")

        print(f"Location     : {city}, {country}")
        print(f"Temperature  : {temp_c:.1f} °C")
        print(f"Temperature  : {temp_f:.1f} °F")
        print(f"Humidity     : {humidity}%")
        print(f"Condition    : {condition.title()}")
        print(f"Wind Speed   : {wind_speed} m/s")

        print("================================")

    except requests.exceptions.Timeout:
        print("Error: Request timed out!")

    except requests.exceptions.ConnectionError:
        print("Error: Check your internet connection!")

    except requests.exceptions.HTTPError as error:
        print("Weather API error:", error)

    except requests.exceptions.RequestException as error:
        print("Network error:", error)

    except (KeyError, ValueError):
        print("Error: Unexpected weather data received!")

# Run the application
if __name__ == "__main__":
    get_weather()
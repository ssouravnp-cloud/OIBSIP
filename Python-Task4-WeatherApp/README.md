# 🌦️ Weather App – Python

## 📌 Project Overview

The Weather App is a beginner-level Python application developed as part of the Oasis Infobyte Internship Program.

This application fetches real-time weather information for a user-specified city or ZIP code using the OpenWeatherMap API.

It displays important weather details, including temperature, humidity, weather conditions, and wind speed.

## 🎯 Objective

The main objective of this project is to develop a Python application that retrieves and displays real-time weather information using an external weather API.

## 🛠️ Technologies Used

- Python
- Requests Library
- JSON
- OpenWeatherMap API
- Visual Studio Code

## ✨ Features

- Search weather information using a city name.
- Search weather using a ZIP code.
- Display temperature in Celsius (°C).
- Display temperature in Fahrenheit (°F).
- Display humidity percentage.
- Display weather condition descriptions.
- Display wind speed.
- Handle invalid city names.
- Handle invalid API keys.
- Handle network errors and request timeouts.
- Validate empty user input.

## 📂 Project Structure

```text
WeatherApp/
│
├── main.py
├── config.py
├── config.example.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── screenshots/
    ├── Bangalore-weather.png
    └── Kozhikode-weather.png
```

## ⚙️ Installation and Setup

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the project folder

```bash
cd OIBSIP/Python-Task4-WeatherApp
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure API Key

1. Create a free account on OpenWeatherMap.
2. Generate an API key.
3. Create a file named `config.py`.
4. Add your API key:

```python
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
```

Note: Never upload your actual API key to GitHub.

### Step 5: Run the application

```bash
python main.py
```

## 🌍 Sample Output

```text
================================
       WEATHER APPLICATION
================================

Enter city name or ZIP code: Bangalore

Fetching weather information...

================================
         WEATHER REPORT
================================

Location     : Bengaluru, IN
Temperature  : 26.0 °C
Temperature  : 78.9 °F
Humidity     : 76%
Condition    : Moderate Rain
Wind Speed   : 3.49 m/s

================================
```

*Note: Weather values are examples. Actual results depend on live weather conditions.*

## 📸 Screenshots

Screenshots of the application demonstrating weather information for different cities will be added here.

## 🎓 Internship Details

**Organization:** Oasis Infobyte

**Internship Track:** Python Programming

**Task:** Task 4 – Basic Weather App

**Level:** Beginner

**Developed by:** Sourav NP

## 🚀 Learning Outcomes

Through this project, I learned:

- Python programming fundamentals.
- Working with external APIs.
- Sending HTTP requests using the Requests library.
- Processing JSON responses.
- Exception handling.
- Input validation.
- Real-time data retrieval.

## 📜 Acknowledgement

I would like to thank Oasis Infobyte for providing this internship opportunity and helping me improve my Python programming skills.

---

**Developed by Sourav NP**
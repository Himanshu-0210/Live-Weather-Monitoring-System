import requests
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime
import seaborn as sns
from key import API_KEY  
import os
import csv

sns.set(style="darkgrid")


CITY = "Gwalior"
UNITS = "metric"  

# Data storage
time_data = []
temp_data = []
feels_like_data = []
humidity_data = []
wind_speed_data = []

fig, ax = plt.subplots() # A shortcut function that creates both fig and ax at once.

csv_file = "weather_log.csv"
file_exists = os.path.isfile(csv_file)

# Write headers if file doesn't exist
if not file_exists:
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Time", "Temperature (°C)", "Humidity (%)", "Wind Speed (m/s)"])

# Get weather data with wind 
def get_weather_data():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units={UNITS}"
    print(url)
    response = requests.get(url).json()

    temp = response['main']['temp']
    humidity = response['main']['humidity']
    wind_speed = response['wind']['speed']


    return temp, humidity, wind_speed

# Update plot every frame
def update(frame):
    now = datetime.now().strftime("%H:%M:%S")
    temp, humidity,  wind_speed = get_weather_data()

    # Append data
    time_data.append(now)
    temp_data.append(temp)
    humidity_data.append(humidity)
    wind_speed_data.append(wind_speed)

    # Keep last 20 records
    if len(time_data) > 30:
        time_data.pop(0)
        temp_data.pop(0)
        humidity_data.pop(0)
        wind_speed_data.pop(0)

    # Save to CSV
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([now, temp, humidity, wind_speed])

    # Plot everything
    ax.clear()
    ax.plot(time_data, temp_data, label="Temp (°C)", marker="o")
    ax.plot(time_data, humidity_data, label="Humidity (%)", marker="s")
    ax.plot(time_data, wind_speed_data, label="Wind Speed (m/s)", marker="D")

    ax.set_title(f"Live Weather in {CITY}")
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    plt.xticks(rotation=45)
    plt.tight_layout()
    ax.legend()
    

    # Print in terminal
    print(f"[{now}] Temp: {temp}°C | Humidity: {humidity}% | Wind: {wind_speed} m/s")

# Start animation
ani = FuncAnimation(fig, update, interval=10000)  # every 60 sec
plt.show()
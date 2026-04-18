# 🌦️ Live Weather Monitoring Dashboard

A Python-based real-time weather monitoring project that fetches live weather data using the **OpenWeatherMap API**, visualizes it dynamically with graphs, and stores historical weather logs in CSV format.

## 🚀 Features

* 🌍 Fetches live weather data for a selected city
* 🌡️ Displays Temperature in real-time
* 💧 Tracks Humidity levels
* 💨 Monitors Wind Speed
* 📈 Live animated graph updates every few seconds
* 💾 Automatically saves weather records into CSV file
* 📊 Useful for weather trend analysis and forecasting projects

## 🛠️ Technologies Used

* Python
* Requests
* Matplotlib
* Seaborn
* CSV
* OpenWeatherMap API

## 📂 Project Structure

```bash
├── liveWeather.py      # Main Python script
├── key.py              # API key file
├── weather_log.csv     # Logged weather data
└── README.md           # Project documentation
```

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Install Dependencies

```bash
pip install requests matplotlib seaborn
```

### 3️⃣ Add Your API Key

Create `key.py`

```python
API_KEY = "your_openweathermap_api_key"
```

Get free API key from: https://openweathermap.org/api

### 4️⃣ Run Project

```bash
python liveWeather.py
```

## 📊 Output

* Live graph with:

  * Temperature
  * Humidity
  * Wind Speed

* CSV log file generated automatically:

```csv
Time, Temperature (°C), Humidity (%), Wind Speed (m/s)
```

## 🌍 Current Configurations

```python
CITY = "Gwalior"
UNITS = "metric"
```

You can change city name inside `liveWeather.py`

## 🔮 Future Improvements

* 7-day weather forecasting using ML
* GUI using Tkinter / Streamlit
* Multi-city comparison dashboard
* Rainfall & Pressure monitoring
* Export graphs as reports

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first.

## 📜 License

This project is open-source and free to use.

## 👨‍💻 Author

**Himanshu Upadhyay**

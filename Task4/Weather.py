import tkinter as tk
import requests
import json

def get_weather_data():
    city = city_entry.get()
    api_key = "5b22857b72f63301742fd17687a5d009"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def update_weather_label():
    root.geometry("300x200+550+235")
    data = get_weather_data()
    if data["cod"] == 200:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"].capitalize()
        weather_label.config(
            text=f"Temperature: {temperature}°C\nHumidity: {humidity}%\nDescription: {description}"
        )
    else:
        root.geometry("400x175+500+250")
        weather_label.config(
            text="Weather data not found. \nPlease check the city name or try again later."
        )

root = tk.Tk()
root.title("Weather Forecast")
root.geometry("300x150+550+250")
city_label = tk.Label(root, text="Enter city name:")
city_label.pack(pady=10)

city_entry = tk.Entry(root)
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=update_weather_label)
get_weather_button.pack(pady=10)

weather_label = tk.Label(root, text="", font=("Arial", 14))
weather_label.pack()

root.mainloop()

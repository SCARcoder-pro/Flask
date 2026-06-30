from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API_KEY = "9c2360243c718345bc1a66af4c62ebd9"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    error_message = None

    if request.method == "POST":
        city = request.form.get("city")

        if city:
            url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    "city": data["name"],
                    "temperature": data["main"]["temp"],
                    "description": data["weather"][0]["description"],
                    "icon": data["weather"][0]["icon"]
                }
            else:
                if request.method == "POST":
                    city=request.form.get("city")

                    if city:
                        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
                        response = requests.get(url)

                        if response.status_code == 200:
                            data = response.json()
                            weather_data = {
                                "city": data["name"],
                                "temperature": data["main"]["temp"],
                                "description": data["weather"][0]["description"],
                                "icon": data["weather"][0]["icon"]
                            }
                        else:
                            error_message = "City not found. Please try again."
                    else:
                        error_message = "Please enter a city name."
                return render_template("weather.html", weather=weather_data, error=error_message)
if __name__ == "__main__":
    app.run(debug=True)
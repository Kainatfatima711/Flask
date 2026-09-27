from flask import Flask , render_template , request
import requests

app = Flask(__name__)

API_KEY = "a44ca95cf1c0aa07bf525ab38910af95"

@app.route("/")
def home():
    return render_template("index.html")

@ app.route("/getweather" , methods = ["POST"])
def get_weather():
    city = request.form.get("city" , "").strip()

    if not city:
        return render_template(
            "index.html",
            error = "Please enter a city name."
        )

    try:
        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}"
            f"&appid = {API_KEY}"
            f"&units = metrics"
        )

        response = requests.get(url)
        weather_data = response.json()
        if weather_data.get("cod") !=200:


            return render_template(
                "index.html",
                error = "City not found."
            )


        data = {
                 "location": weather_data["name"],
                 "country_code": weather_data["sys"]["country"],
                 "temp": weather_data["main"]["temp"],
                 "humidity": weather_data["main"]["humidity"],
                 "description":weather_data["weather"][0]["description"]
                }

        return render_template(
            "index.html",
            data = data
        )

    except Exception:
        return render_template(
            "index.html",
            error = "Something went wrong."
        )
        
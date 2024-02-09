from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(city, country):
    try:
        api_key = "d077ff93d6964798a2d230305240702"
        base_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city},{country}&aqi=no"

        response = requests.get(base_url)
        data = response.json()

        if "error" not in data:
            return data
        else:
            return {"error": "City not found."}
    except requests.RequestException as e:
        return {"error": f"Failed to retrieve weather data: {e}"}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form["city"].strip()
        country = request.form["country"].strip()
        weather_data = get_weather(city, country)
        if "error" in weather_data:
            return render_template("html_1.html", error=weather_data["error"])
        else:
            return render_template("html_1.html", weather=weather_data, city=city)

    return render_template("html_1.html")

if __name__ == "__main__":
    app.run(debug=True)

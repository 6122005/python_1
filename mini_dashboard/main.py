import os
from datetime import datetime

import requests
from dotenv import load_dotenv


load_dotenv()

NEWS_API_KEY = os.getenv("b6e7c13caa3d46408114020f923d2d8b")


# -----------------------------
# TIME
# -----------------------------
def get_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# -----------------------------
# WEATHER
# -----------------------------
def get_weather():
    """
    Surat Coordinates
    Latitude  : 21.1702
    Longitude : 72.8311
    """

    try:
        url = (
            "https://api.open-meteo.com/v1/forecast"
            "?latitude=21.1702"
            "&longitude=72.8311"
            "&current_weather=true"
        )

        response = requests.get(url, timeout=10)

        response.raise_for_status()

        data = response.json()

        weather = data["current_weather"]

        return {
            "temperature": weather["temperature"],
            "windspeed": weather["windspeed"]
        }

    except requests.exceptions.Timeout:
        return {"error": "Weather API Timeout"}

    except requests.exceptions.ConnectionError:
        return {"error": "No Internet Connection"}

    except Exception as e:
        return {"error": str(e)}


# -----------------------------
# NEWS
# -----------------------------
def get_news():
    try:

        url = (
            f"https://newsapi.org/v2/top-headlines?"
            f"country=us&"
            f"pageSize=5&"
            f"apiKey={NEWS_API_KEY}"
        )

        response = requests.get(url, timeout=10)

        response.raise_for_status()

        data = response.json()

        articles = data.get("articles", [])

        headlines = []

        for article in articles:
            headlines.append(article["title"])

        return headlines

    except requests.exceptions.Timeout:
        return ["News API Timeout"]

    except requests.exceptions.ConnectionError:
        return ["No Internet Connection"]

    except Exception as e:
        return [str(e)]


# -----------------------------
# DASHBOARD
# -----------------------------
def show_dashboard():

    print("\n" + "=" * 40)
    print("      🚀 MY CLI DASHBOARD")
    print("=" * 40)

    print("\n🕒 Current Time")
    print("-" * 20)
    print(get_time())

    weather = get_weather()

    print("\n🌦️ Weather")
    print("-" * 20)

    if "error" in weather:
        print(weather["error"])

    else:
        print("City: Surat")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Wind Speed: {weather['windspeed']} km/h")

    print("\n📰 Top News")
    print("-" * 20)

    news = get_news()

    for index, headline in enumerate(news, start=1):
        print(f"{index}. {headline}")

    print("\n" + "=" * 40)


if __name__ == "__main__":
    show_dashboard()
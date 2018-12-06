import requests
from bs4 import BeautifulSoup
import pandas as pd



"""Gets page request and stores the content"""
def getPageRequest():

    newYork = "https://forecast.weather.gov/MapClick.php?lat=40.7146&lon=-74.0071"
    meadville = "https://forecast.weather.gov/MapClick.php?lat=41.63648000000006&lon=-80.15142999999995"
    city = input("Which city you which to know the weather for ? New York or Meadville : ")
    if city == "new york":
        page = requests.get(newYork)
        soup = BeautifulSoup(page.content, 'html.parser')

    elif city == "meadville":
        page = requests.get(meadville)
        soup = BeautifulSoup(page.content, 'html.parser')
    else:
        return "please invalid city "
    return soup


    # page = requests.get("https://forecast.weather.gov/MapClick.php?lat=40.7146&lon=-74.0071")
    # soup = BeautifulSoup(page.content, 'html.parser')
    # return soup


"""Finds the weather table using id/class tags."""
def weeklyWeather(soup):
    seven_day = soup.find(id="seven-day-forecast")
    forecast_items = seven_day.find_all(class_="tombstone-container")
    tonight = forecast_items[0]
    return seven_day

"""Gets the day of the week"""
def weekdays(seven_day):
    period_tags = seven_day.select(".tombstone-container .period-name")
    periods = [pt.get_text() for pt in period_tags]
    return periods


"""Stores short discriptions of each day's weather"""
def getShortDescription(seven_day):
    short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
    return short_descs


"""Stores the weather"""
def getTemp(seven_day):
    temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
    return temps

"""stores each day discription"""
# def getDescription(seven_day):
#     descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
#     return descs

""" Creates table"""
def createTable(periods, short_descs, temps):
    weather = pd.DataFrame({
            "Day": periods,
            "short description": short_descs,
            "temperature": temps
            # "full description":descs
        })
    weather.to_csv('../build/weather.csv')

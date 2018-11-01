import requests
from bs4 import BeautifulSoup

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
page.status_code
page.content
soup = BeautifulSoup(page.content, 'html.parser')

seven_day = soup.find(id="seven-day-forecast")
forecast_item = seven_day.find_all(class_="tombstone-container")
tonight = forecast_item[0]
"""print(tonight.prettify())"""

period = tonight.find(class_="period-name").get_text()
temp = tonight.find(class_="temp").get_text()
short_des = tonight.find(class_="short-desc").get_text()

print(period)
print(temp)
print(short_des)

""" extract title """

img = tonight.find("img")
desc = img['title']

print(desc)

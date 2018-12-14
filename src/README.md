
# Weather Web Scraper

This is a web scrapper program that uses a variety of python libraries to scrap
and store weather data from the National Weather Service. The Program scraps
the weekly weather information from Meadvile and New York City. The user most
specify witch place they want to know the weather from. The data is then stored
in a csv file and then the program displays the data stored in the csv file
using a python GUI library. The goal of this program was to become more familiar
with python and see how simpler it was to web scrap data using python libraries
than other programming languages. The next step is to branch out, and combine
machine learning with web scraping. My idea is to create a stock market bot that
uses machine learning and stock market data to invest money.

## How to build and run web scraper & Software tools used

In order to build the web scraper Python 3.0 or higher is recommended. Some
of the libraries only work with python 3.0. The two main libraries used to get
the information from the National Weather Service were `requests` and
`beautifulsoup4` I use the `request` library to make a `GET` request to the
National weatherService web server which allow us to get the `HTML` content. I
then use `beautifulsoup4`to parse the `HTML` content and extract the text. In
order to find out what data I wanted to extract, I inspected the sources code to
see in which class or id tags the weather dat was. I used the `find and find_all`
 methods from`beautifulsoup4` library to get the `HTML` content and then used
`get_text` method to extract the text. To store the data I used `pandas` a
Pythonlibrary that makes it easy to analysis data and create data frames. I
used the library to create a data frame and then save it in csv file. Finally
I used `tkinter` I library to make simple GUI windows to display the weather
data. The program into two separate classes, `WeatherData.py` and `main.py`. In
order to run the program you will need the following libraries installed:
`pip install --upgrade pip`, `pip install beautifulsoup4`,
`pip install requests`, `pip install --upgrade pandas`, and `pip install imgkit`
.If you have multiple versions of python installed, you want to specify
version 3: `python3 main.py`.

### Tangible results

![CSV](/build/csv.png)
![GUI](/build/GUI.png)

### How to test the web scraper

To test the weather web scraper you can try different cities to see how it
handles different weathers. First you will need to go to
`https://www.weather.gov/` type the city you want and then copy the `URL`.
Then open the `weatherDataForTravisBuild.py` and in the `page = requests()`
replace the `URL` that is there with yours.

One downside to the web scrapper is that when there is weather storms or alerts.
The web scraper can't handle the extra text around the tags or id so you will
get an error and the program will not run. If you come across this issue, please
try a different place.

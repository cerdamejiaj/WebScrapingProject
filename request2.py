import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
page.status_code
page.content

soup = BeautifulSoup(page.content, 'html.parser')

"""soup.find_all('p')[0].get_text()"""

"""print(soup.prettify())"""

"""print(soup)"""


""" searching for tags by class and id """
byClass = soup.find_all('p', class_= 'outer-text')
byID = soup.find_all(id="first")
"""print(byClass)
print(byID)"""


"""Using CSS Selectors """

css = soup.select("div p")
print(css)

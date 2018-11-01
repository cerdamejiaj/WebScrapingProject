import requests
from bs4 import BeautifulSoup


""" Makes Get resques to a web server and downloads the hmtl content"""

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
page.status_code
page.content

soup = BeautifulSoup(page.content, 'html.parser')
"""print(soup.prettify())"""
"""print(list(soup.children))
print([type(item) for item in list(soup.children)])
"""

html = list(soup.children)[2]
(list(html.children))

body = list(html.children)[3]

"""print(list(body.children))"""

p = list(body.children)[1]
print(p.get_text())

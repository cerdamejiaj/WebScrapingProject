import requests


""" Makes Get resques to a web server and downloads the hmtl content"""

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
page.status_code
page.content

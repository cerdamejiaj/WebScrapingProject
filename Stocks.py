import requests
from bs4 import BeautifulSoup
import pandas as pd




def requestingPageContent():
    page = requests.get("https://www.suredividend.com/technology-stocks-list/")
    soup = BeautifulSoup(page.content, 'html.parser')
    StockChart = soup.find(id="table_1")
    print(StockChart)

requestingPageContent()

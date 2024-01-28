import os
import time

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Accept-Language": "en-IN,en;q=0.9"
}

zillow_link = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.54782763842773%2C%22east%22%3A-122.31883136157226%2C%22south%22%3A37.668295313786096%2C%22north%22%3A37.882133967348146%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

Gform_link = os.environ.get("GFORM")

response = requests.get(url=zillow_link, headers=header).text

soup = BeautifulSoup(response, "html.parser")

addresses = []
prices = []
links = []

find_addresses = soup.select(selector=".property-card-data a address")

for ad in find_addresses:
    addresses.append(ad.get_text())

find_prices = soup.select(selector=".PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1")

for pr in find_prices:
    prices.append(pr.get_text().split("+")[0].split("/")[0])

find_links = soup.select(selector=".property-card-data a")

for li in find_links:
    link = li["href"]
    extra = "https://www.zillow.com"
    if extra not in link:
        link = f"{extra}{link}"
    links.append(link)

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option)
driver.maximize_window()

driver.get(url=Gform_link)

for i in range(len(prices)):
    driver.get(url=Gform_link)

    input_address = driver.find_element(By.XPATH,
                                        '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input_address.send_keys(addresses[i])
    time.sleep(1)

    input_price = driver.find_element(By.XPATH,
                                      '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input_price.send_keys(prices[i])

    input_link = driver.find_element(By.XPATH,
                                     '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input_link.send_keys(links[i])

    submit = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span')
    driver.execute_script("arguments[0].click()", submit)
    time.sleep(3)
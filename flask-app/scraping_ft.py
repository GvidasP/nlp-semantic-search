import random

from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import time
import re
import os

starting_point = 1
ending_point = 8
batch_size = 8

for j in range(600):
    print(f'# starting {j} cycle')

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options,
                              executable_path="C:/Users/gvida/Desktop/studies/naturalios_kalbos_apdorojimas/1uzduotis/chromedriver.exe")

    data_list = []
    for i in range(starting_point, ending_point + 1):
        print(f'#\tworking on page {i}')

        driver.get("https://www.ft.com/world?page=" + str(i))
        driver.implicitly_wait(20)
        html_source_code = driver.execute_script("return document.body.innerHTML;")
        soup = BeautifulSoup(html_source_code, 'html.parser')

        news = soup.find(class_=re.compile("o-teaser-collection__list"))

        tags_html = news.find_all(class_=re.compile("(o-teaser__meta)"))
        headlines_html = news.find_all(class_=re.compile("(o-teaser__heading)"))
        summaries_html = news.find_all(class_=re.compile("(o-teaser__standfirst)"))

        for tag, headline, summary in zip(tags_html, headlines_html, summaries_html):
            data_list.append({"Tag": tag.get_text(), "Headline": headline.get_text(), "Summary": summary.get_text(),
                              "Link": f"https://www.ft.com{headline.a.get('href')}"})

    articles_dataframe = pd.DataFrame(data=data_list, columns=["Tag", "Headline", "Summary", "Link"])
    articles_dataframe.to_csv(f'data/articles{j}.csv', index=False, encoding="utf-8")

    print(f'# cycle {j} finished')

    starting_point = ending_point + 1
    ending_point += batch_size

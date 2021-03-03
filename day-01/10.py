from bs4 import BeautifulSoup
import requests
from IPython import embed
import time
import numpy as np

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"}

time.sleep(2)

BASE_URL="https://albertyumol.github.io/"

def extract_html_content(target_url):
    response=requests.get(target_url, headers)
    return response.text

def main():
    target_page=BASE_URL + "index.html"

    html_content=extract_html_content(target_page)

    soup = BeautifulSoup(html_content, "html.parser")
    # a_elements = soup.find_all("a", {"rel": "permalink"})
    # for a_element in a_elements:
    #     print(a_element.get_text())

    list_div = soup.find_all("div", "list__item")

    for list_item in list_div:
        print(list_item.find("a").get_text("href"))

    for i in np.arange(2, 5):
        target_page=BASE_URL + "page" + str(i)
        html_content=extract_html_content(target_page)

        soup = BeautifulSoup(html_content, "html.parser")

        list_div = soup.find_all("div", "list__item")

        for list_item in list_div:
            print(list_item.find("a").get_text("href"))

if __name__ == "__main__":
    main()
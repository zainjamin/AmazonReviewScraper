from math import ceil
import requests
from bs4 import BeautifulSoup
import pandas as pd


class AmazonReviewScraper:
    def __init__(self, item):
        self.__item_id = item
        self.__name_list = []
        self.__review_list = []

    @staticmethod
    def __html_code(url):
        headers = ({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) \
                                AppleWebKit/537.36 (KHTML, like Gecko) \
                                Chrome/102.0.0.0 Safari/537.36',
                    'Accepted-Language': 'en-US, en;q=0.5'})
        htmldata = requests.get(url, headers=headers).text
        soup = BeautifulSoup(htmldata, 'html.parser')
        return soup

    @staticmethod
    def __num_pages(soup):
        page_content = soup.find_all("div", {"data-hook": "cr-filter-info-review-rating-count"})
        review_count = int(page_content[0].get_text().strip().replace('| ', '').split(" ")[3].replace(',', ''))
        return ceil(review_count / 10)

    def __find_names(self, soup):
        data = soup.find_all("div", {"data-hook": "review"})
        for item in data:
            name = item.find_next("span", {"class": "a-profile-name"}).get_text()
            self.__name_list.append(name)
            review = item.find_next("span", {"data-hook": "review-body"}).get_text().replace('\n', '')
            self.__review_list.append(review)

    def scrape(self):
        base_url = 'https://www.amazon.ca/product-reviews/{}/ref' \
                   '=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={}'
        soup = self.__html_code(base_url.format(self.__item_id, '1'))
        page_count = self.__num_pages(soup)
        for i in range(1, min(501, page_count + 1)):
            print("Now on page " + str(i))
            soup = self.__html_code(base_url.format(self.__item_id, str(i)))
            self.__find_names(soup)

    def to_csv(self):
        data = {"Name": self.__name_list, "Review": self.__review_list}
        pd.DataFrame(data).to_csv('reviews.csv')


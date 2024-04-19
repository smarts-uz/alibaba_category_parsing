import requests
from bs4 import BeautifulSoup
# import yaml



def parse_russian_alibaba(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    categories_lists = soup.find('div', class_='cg-main')
    categories_container = soup.find_all('div', class_='item util-clearfix')
    for id,category_container in enumerate(categories_container[:1]):
        parent_category_name = category_container.find('h3').text
        # D = parent_category_name_container.fin
        # print(id,parent_category_name.strip())
        sub_categories_container = category_container.find_all('div', class_='sub-item')
        for sub_id,sub_category_container in enumerate(sub_categories_container[:1]):
            sub_category_name = sub_category_container.find('h4',class_='sub-title').find('a').get_text(strip=True)
            child_category_container = sub_category_container.find('ul', class_='sub-item-cont util-clearfix')
            child_categories = child_category_container.find_all('li')
            for child_category in child_categories:
                child_category_name = child_category.find('a').get_text(strip=True)
                print(child_category_name)








parse_russian_alibaba(url='https://russian.alibaba.com/products')



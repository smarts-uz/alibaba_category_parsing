import requests
import os
from bs4 import BeautifulSoup
import yaml
def parse_russian_alibaba(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    categories_container = soup.find_all('div', class_='item util-clearfix')
    all_categories = []
    for category_container in categories_container:
        parent_category_name = category_container.find('h3').text.strip()
        sub_categories_container = category_container.find_all('div', class_='sub-item')
        for sub_category_container in sub_categories_container:
            sub_category_name = sub_category_container.find('h4', class_='sub-title').find('a').get_text(strip=True)
            child_category_container = sub_category_container.find('ul', class_='sub-item-cont util-clearfix')
            child_categories = child_category_container.find_all('li')
            for child_category in child_categories:
                child_category_name = child_category.find('a').get_text(strip=True)
                all_categories.append({"parent": parent_category_name,
                                       "sub": sub_category_name,
                                       "child": child_category_name})

    return all_categories

categories = parse_russian_alibaba(url='https://russian.alibaba.com/products')
#  Reason bunaqa format kegusida file paths sifatida foydalanishimiz uchun shu formatda yigildi yani mhtml yoki html larni saveing location sifatida

# you can see every Category names

# for category in categories:
#     print(category)

# Write categories to a YAML file
path='categories.yaml'
if os.path.exists(path):
    print(f'The file:{path} already exists')
else:
    print(f'The file:{path} does not exist')
    with open('categories.yaml', 'w') as file:
        yaml.dump(categories, file)
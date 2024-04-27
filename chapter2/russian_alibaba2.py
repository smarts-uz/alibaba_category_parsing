import requests
import os
from bs4 import BeautifulSoup
import yaml

def parse_russian_alibaba(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    categories_container = soup.find_all('div', class_='item util-clearfix')
    all_categories = {}
    for category_container in categories_container:
        parent_category_name = category_container.find('h3').text.strip()
        sub_categories_container = category_container.find_all('div', class_='sub-item')
        all_categories[parent_category_name] = {}
        for sub_category_container in sub_categories_container:
            sub_category_name = sub_category_container.find('h4', class_='sub-title').find('a').get_text(strip=True)
            child_category_container = sub_category_container.find('ul', class_='sub-item-cont util-clearfix')
            all_categories[parent_category_name][sub_category_name] = []
            child_categories = child_category_container.find_all('li')
            for child_category in child_categories:
                child_category_name = child_category.find('a').get_text(strip=True)
                all_categories[parent_category_name][sub_category_name].append(child_category_name)

    return all_categories

def main():
    categories = parse_russian_alibaba(url='https://russian.alibaba.com/products')

    # Fayl nomi
    file_path = 'categories.yaml'

    # Fayl mavjudligini tekshirish
    if os.path.exists(file_path):
        print(f'The file: {file_path} already exists.')
        print(f'Updating {file_path}...')
    else:
        print(f'The file: {file_path} does not exist.')
        print(f'Creating {file_path}...')

    # YAML faylni yaratish Va yangilash
    with open(file_path, 'w', encoding='utf-8') as file:
        yaml.dump(categories, file, allow_unicode=True)

    print(f'File {file_path} successfully created/updated.')

if __name__ == "__main__":
    main()
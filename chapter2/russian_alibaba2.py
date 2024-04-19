import requests
from bs4 import BeautifulSoup

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
                all_categories.append(f"{parent_category_name}\\{sub_category_name}\\{child_category_name}")

    # print(all_categories)
    return  all_categories

categories=parse_russian_alibaba(url='https://russian.alibaba.com/products')

#  Reason bunaqa format kegusida file paths sifatida foydalanishimiz uchun shu formatda yigildi yani mhtml yoki html larni saveing location sifatida
for category in categories:
    print(category)




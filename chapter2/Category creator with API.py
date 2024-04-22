import requests
import os
from bs4 import BeautifulSoup
from woocommerce import API
import yaml
#
# # WC API ni yaratish
# wcapi = API(
#     url="https://globmarketplace.com/ru/",
#     consumer_key="ck_3a6bd6bf3484322bc28eca2787af2332df2e29ec",
#     consumer_secret="cs_3e7f36edc1c1012786049cc48647d55b62358d8c"
# )
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
#

# WC API ni yaratish
# wcapi = API(
#     url="https://globmarketplace.com/ru/",
#     consumer_key="ck_019eeb344f39579df759e04f6f96c522fe3b896b",
#     consumer_secret="cs_5127afd22c791c8ce0d56a596b8f7d9d959d0c96"
#     )
wcapi = API(
        url="http://localhost:10022",
        consumer_key="ck_8351c208208b8ea59914dce89a22e462c269bca0",
        consumer_secret="cs_627180930e1fea8e73467fc356574e0ad280d53a")
def create_categories(categories, parent=0):
    # Agar categories ro'yxati ro'yxat bo'lsa
    if isinstance(categories, list):
        for sub_categories in categories:
            create_categories(sub_categories, parent=parent)
    # Agar categories ro'yxati obyekt bo'lsa
    elif isinstance(categories, dict):
        for category_name, sub_categories in categories.items():
            # Kategoriyani yaratish
            data = {
                "name": category_name,
                "parent": parent
            }
            response = wcapi.post("products/categories", data).json()
            category_id = response.get("id")

            print(f"Category '{category_name}' created with ID {category_id}")

            # Agar ichki kategoriyalar mavjud bo'lsa, ularga qo'shish
            if sub_categories:
                create_categories(sub_categories, parent=category_id)
    else:
        print("Invalid categories format!")

def main():
    # Kategoriyalarni olish
    categories = parse_russian_alibaba(url='https://russian.alibaba.com/products')
    #
    # # WC API ni yaratish
    # wcapi = API(
    #     url="http://localhost:10022",
    #     consumer_key="ck_8351c208208b8ea59914dce89a22e462c269bca0",
    #     consumer_secret="cs_627180930e1fea8e73467fc356574e0ad280d53a"
    # )

    # Bosh kategoriyalarni yaratish
    create_categories(categories)

if __name__ == "__main__":
    main()





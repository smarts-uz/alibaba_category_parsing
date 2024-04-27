import time
import os
import yaml
from woocommerce import API

wcapi = API(
    url="https://globmarketplace.com/ru/",
    consumer_key="ck_3a6bd6bf3484322bc28eca2787af2332df2e29ec",
    consumer_secret="cs_3e7f36edc1c1012786049cc48647d55b62358d8c"
)

def create_category(category_data, parent_category_id=0):
    # Check if category exists
    existing_categories = wcapi.get("products/categories").json()
    category_name = category_data["name"]
    for category in existing_categories:
        if category["name"] == category_name:
            print(f"Category '{category_name}' already exists.")
            return category["id"]

    # Create new category
    image_url = category_data.get("image", "").get("src", "")
    data = {
        "name": category_name,
        "parent": parent_category_id,
        "image": {"src": image_url}
    }
    try:
        response = wcapi.post("products/categories", data).json()
        category_id = response.get("id")
        print(f"Category '{category_name}' created successfully with ID: {category_id}")
        return category_id
    except Exception as e:
        print(f"Error creating category '{category_name}': {e}")
        return None

with open("categories.yaml", "r") as file:
    categories = yaml.safe_load(file)

for category_data in categories:
    create_category(category_data)
    # print(category_data)



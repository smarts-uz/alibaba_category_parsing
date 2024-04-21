import time
import os
import yaml
from woocommerce import API

wcapi = API(
    # url="http://dev.smarts.uz",
    # consumer_key="ck_16732ed59606bc5dae86cfb485a99d9137ad38a1",
    # consumer_secret="cs_84419bd230bb13a05331461aab57e4782466a0fa"
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

def main():
    with open("categories.yaml", "r") as file:
        categories = yaml.safe_load(file)

    for category_data in categories:
        create_category(category_data)
        # print(category_data)

if __name__ == "__main__":
    main()
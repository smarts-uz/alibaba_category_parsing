# import yaml
# import requests
#
#
# def read_categories_from_yaml(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         categories = yaml.safe_load(file)
#     return categories
#
#
# def create_category(url, consumer_key, consumer_secret, category_name, parent_id=None):
#     data = {
#         "name": category_name,
#         "parent": parent_id
#     }
#     response = requests.post(url + "/wp-json/wc/v3/products/categories", auth=(consumer_key, consumer_secret),
#                              json=data)
#     if response.status_code > 201:
#         print(f"Category '{category_name}' created successfully! with{parent_id}")
#     else:
#         print(f"Failed to create category '{category_name}'. Status code: {response.status_code}")
#
#
# def create_categories_from_yaml(file_path, url, consumer_key, consumer_secret, parent_id=None):
#     categories = read_categories_from_yaml(file_path)
#     if isinstance(categories, dict):
#         for category_name, sub_categories in categories.items():
#             category_id = create_category(url, consumer_key, consumer_secret, category_name, parent_id)
#             create_categories_from_yaml(file_path, url, consumer_key, consumer_secret, category_id)
#     elif isinstance(categories, list):
#         for category_name in categories:
#             create_category(url, consumer_key, consumer_secret, category_name, parent_id)
#
#
# def main():
#     # Woocommerce REST API ma'lumotlari
#     url = "http://localhost:10017"
#     consumer_key = "ck_01257f5dbb2c4a169d9e2b28b2d0273ce40f0440"
#     consumer_secret = "cs_a4408800c3e70c0a97b6e80d8a4402581d57a4a4"
#
#     # YAML fayli
#     yaml_file = "categories.yaml"
#
#     # Kategoriyalarni yaratish
#     create_categories_from_yaml(yaml_file, url, consumer_key, consumer_secret)
#
#
# if __name__ == "__main__":
#     main()

#  faqat Parrent Categorylar uchun
# import yaml
# import requests
#
#
# def create_category(url, consumer_key, consumer_secret, category_name, parent_id=None):
#     data = {
#         "name": category_name,
#         "parent": parent_id
#     }
#     response = requests.post(url + "/wp-json/wc/v3/products/categories", auth=(consumer_key, consumer_secret), json=data)
#
#     if response.status_code > 201:
#         print(f"Category '{category_name}' created successfully!")
#         return response.json().get('id')
#     else:
#         print(f"Failed to create category '{category_name}'. Status code: {response.status_code}")
#         return None
#
#
# def create_categories_from_yaml(file_path, url, consumer_key, consumer_secret, parent_id=None):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         categories = yaml.safe_load(file)
#
#     if categories is None:
#         print("No categories found in the YAML file.")
#         return
#
#     if not isinstance(categories, dict):
#         print("Invalid YAML format. Expected a dictionary of categories.")
#         return
#
#     for parent_category, sub_categories in categories.items():
#         parent_category_id = create_category(url, consumer_key, consumer_secret, parent_category, parent_id)
#         if parent_category_id:
#             if isinstance(sub_categories, list):
#                 for sub_category in sub_categories:
#                     create_category(url, consumer_key, consumer_secret, sub_category, parent_category_id)
#             else:
#                 print("Invalid sub-categories format. Expected a list.")
#
# url = "http://localhost:10022"
# consumer_key = "ck_8351c208208b8ea59914dce89a22e462c269bca0"
# consumer_secret = "cs_627180930e1fea8e73467fc356574e0ad280d53a"
# def main():
#     # Woocommerce REST API ma'lumotlari
#
#
#     # YAML fayli
#     yaml_file = "categories.yaml"
#
#     # Kategoriyalarni yaratish
#     create_categories_from_yaml(yaml_file, url, consumer_key, consumer_secret)
#
#
# if __name__ == "__main__":
#     main()

import yaml
import requests


def create_category(url, consumer_key, consumer_secret, category_data):
    response = requests.post(
        f"{url}/wp-json/wc/v3/products/categories",
        auth=(consumer_key, consumer_secret),
        json=category_data
    )

    print(f"Category '{category_data['name']}' created successfully!")
    return response.json().get('id')
    # else:
    #     print(f"Failed to create category '{category_data['name']}'. Status code: {response.status_code}")
    #     return None


def create_categories_from_yaml(file_path, url, consumer_key, consumer_secret, parent_id=None):
    with open(file_path, 'r', encoding='utf-8') as file:
        categories = yaml.safe_load(file)

    if categories is None:
        print("No categories found in the YAML file.")
        return

    if not isinstance(categories, dict):
        print("Invalid YAML format. Expected a dictionary of categories.")
        return

    for parent_category, sub_categories in categories.items():
        parent_category_id = create_category(url, consumer_key, consumer_secret,
                                             {"name": parent_category, "parent": parent_id})
        if parent_category_id:
            if isinstance(sub_categories, dict):
                for sub_category, child_categories in sub_categories.items():
                    sub_category_id = create_category(url, consumer_key, consumer_secret,
                                                      {"name": sub_category, "parent": parent_category_id})
                    if sub_category_id:
                        if isinstance(child_categories, list):
                            for child_category in child_categories:
                                create_category(url, consumer_key, consumer_secret,
                                                {"name": child_category, "parent": sub_category_id})
                        else:
                            print(f"Invalid format for child categories of '{sub_category}'. Expected a list.")
            else:
                print(f"Invalid format for sub categories of '{parent_category}'. Expected a dictionary.")


def main():
    # Woocommerce REST API ma'lumotlari
    url = "http://localhost:10022"
    consumer_key = "ck_8351c208208b8ea59914dce89a22e462c269bca0"
    consumer_secret = "cs_627180930e1fea8e73467fc356574e0ad280d53a"

    # YAML fayli
    yaml_file = "categories.yaml"

    # Boshlang'ich kategoriya yaratish
    create_categories_from_yaml(yaml_file, url, consumer_key, consumer_secret)


if __name__ == "__main__":
    main()
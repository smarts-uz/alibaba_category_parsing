from woocommerce import API
import yaml

# Woocommerce ma'lumotlari
url = "https://globmarketplace.com/ru/"
consumer_key = "ck_3a6bd6bf3484322bc28eca2787af2332df2e29ec"
consumer_secret = "cs_3e7f36edc1c1012786049cc48647d55b62358d8c"

# Kategoriyalarni YAML fayldan o'qish
with open("categories.yaml", "r") as file:
    categories = yaml.safe_load(file)

# WC API ni yaratish
wcapi = API(
    url=url,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    version="wc/v3"
)

def create_categories(categories, parent=0):
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

def main():
    # Bosh kategoriyalar yaratish
    create_categories(categories)

if __name__ == "__main__":
    main()
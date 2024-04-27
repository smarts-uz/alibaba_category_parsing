import yaml


c_k ="ck_9e728422417c952acdce66bdab82f587b5e4c6cd"
c_c = "cs_40ec3cff6db7bae726c10a3b352de8a813655abb"
from woocommerce import API


wcapi = API(
    url="http://mysite.local",
    consumer_key=c_k,
    consumer_secret=c_c
)
print(wcapi.get("products/categories").json())
def add_category():
    with open('categories.yaml', 'r') as f:
        data = yaml.safe_load(f)
        # pprint(data)
    for category in data:
        print(1, category)
        for subcategory in data[category]:
            print(2, subcategory)
            for subsubcategory in data[category][subcategory]:
                print(3, subsubcategory)



# add_category()
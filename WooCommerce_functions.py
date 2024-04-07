import time
import os
from woocommerce import API
from pprint import pprint
from  rich import print
import json
from url_text import create_json_response

wcapi = API(
    url="http://dev.smarts.uz",
    consumer_key="ck_16732ed59606bc5dae86cfb485a99d9137ad38a1",
    consumer_secret="cs_84419bd230bb13a05331461aab57e4782466a0fa"
)

def create_category(category_listdir,cat_id=0,img=False):
    if img == False:
        image = ''
    else:
        with open(f'{category_listdir}/all.json','r') as f:
            data = json.load(f)
            image = data['imageUrl'].replace('//','')

    with open(f"{category_listdir}/ru.txt", 'r') as f:
        parent_category_name = f.read()
        data = {
        "name": parent_category_name,
        "image": {
            "src": image
        },
        "parent": cat_id
    }
        if os.path.exists(f"{category_listdir}/Response.json"):
            print('Category already exists')
        else:
            try:
                response = wcapi.post("products/categories", data).json()
                time.sleep(0.01)
            except Exception as e:
                print(e)
                time.sleep(20)
                response = wcapi.post("products/categories", data).json()

            print(f'Category created {parent_category_name} successfully')
            create_json_response(src=category_listdir, response=response)
        with open(f"{category_listdir}/response.json", 'r') as f:
            data = json.load(f)
            try:
                category_id = data['id']
            except:
                category_id = data['data']['resource_id']
        return category_id

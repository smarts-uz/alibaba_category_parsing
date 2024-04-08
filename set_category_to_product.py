import os.path

import requests
import json

url = "https://dev.smarts.uz/wp-json/wc/v3/products/batch"
l = 0
rand = 577
rand_1 = 660
rand_2 = 617
rand_3 = 617
with open('Products/product.json',mode='r',encoding='utf-8') as file:
    data = json.load(file)
    for product in data:
        product_id = product['id']
        name = product['name']
        with open('Category_number.json',mode='r',encoding='utf-8') as file:
            cat_data = json.load(file)
            for cat,value in cat_data[l].items():
                parent_category_id = value['parent_category_id']
                sub_category_id = value['sub_category_id']
                child_category_id = value['child_category_id']
                # print(parent_category_id, sub_category_id, child_category_id)
                payload = json.dumps({
                  "update": [
                    {
                      "id": product_id,
                      "categories": [
                        {
                          "id": rand
                        },
                        {
                          "id": rand_1
                        },{
                          "id": rand_2
                        },{
                          "id": rand_3
                        },
                        {
                          "id": child_category_id
                        }
                      ]
                    }
                  ]
                })
                headers = {
                  'Content-Type': 'application/json',
                  'Authorization': 'Basic Y2tfYjA2ODIwMmI3M2ViZTQ1MDU3YjkzYjVkNDQ3NTYxNDc1NDE3OWUyNzpjc18xOWNiODc5Zjk4NzA4OTViZWViNTM5MDk3NjVlY2UyYTU1MDE1Nzdi'
                }
                if os.path.exists(f'batch-update-products/{name}.json'):
                    print(f'{l}).{product_id} category already set')
                else:
                    response = requests.request("POST", url, headers=headers, data=payload,verify='ssl/dev.smarts.uz.crt').json()
                    with open(f'batch-update-products/{name}.json',mode='w',encoding='utf-8') as file:
                        json_data = json.dumps(response, indent=4, ensure_ascii=False)
                        file.write(json_data)
                    print(f'{l}:{name} Category set!!!!!')


            l += 1
            rand +=1
            rand_1 -=1
            rand_2+=1
            rand_3-=1




# print(response.text)
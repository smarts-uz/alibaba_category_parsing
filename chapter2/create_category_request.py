
from pprint import pprint
import requests
import json

url = "https://globmarketplace.com/wp-json/wc/v3/products/categories"

c_k ="ck_9e728422417c952acdce66bdab82f587b5e4c6cd"
c_c = "cs_40ec3cff6db7bae726c10a3b352de8a813655abb"
def send_request_api(cat_name,path,parent_id=0):
    print(f'path: {path}')
    payload = json.dumps({
        "name": cat_name,
        "parent": int(parent_id)
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic Y2tfOWU3Mjg0MjI0MTdjOTUyYWNkY2U2NmJkYWI4MmY1ODdiNWU0YzZjZDpjc180MGVjM2NmZjZkYjdiYWU3MjZjMTBhM2IzNTJkZThhODEzNjU1YWJi',
        'Cookie': 'wcpay_currency=ZAR_1',

    }

    response = requests.request("POST", url, headers=headers, data=payload,verify=False,timeout=60)
    response.encoding = 'UTF-8'
    with open(f'{path}/{cat_name.strip()}.json', 'w') as f:
        data = json.dumps(response.json(),indent=4)
        f.write(data)


    try:
        # pass
        category_id = response.json()['id']
        print(f'{cat_name} has been created id:{category_id}')
    except Exception as e:
        category_id = response.json()['data']['resource_id']
        print(f'{cat_name} already exists id:{category_id}')

    return category_id

import json
import os
import time

import mysql.connector
from woocommerce import API


wcapi = API(
    url="http://dev.smarts.uz",
    consumer_key="ck_16732ed59606bc5dae86cfb485a99d9137ad38a1",
    consumer_secret="cs_84419bd230bb13a05331461aab57e4782466a0fa"
)





def sub_category():
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='localhost',
                                  database='mysql')
    try:
        id_list = []
        cursor = cnx.cursor()
        cursor.execute("""select id,name from categories where parent_id is NULL""")
        result = cursor.fetchall()
        for row in result:
            print(row[1])
            data = {
                "name": row[1],
                "image": {
                    "src": ''
                },
                "parent": 2183,
            }
            if os.path.isfile(f'Useruz/{row[1]}.json'):
                print('Category already exists')
                with open(f'Useruz/{row[1]}.json', 'r') as f:
                    data = json.load(f)
                    category_id = data['id']
            else:
                response = wcapi.post("products/categories", data).json()
                category_id = response['id']
                with open(f'Useruz/{row[1]}.json', 'w') as f:
                    json_object = json.dumps(response, indent=4)
                    f.write(json_object)
                    print(f'[cyan]Created json file')
                id_list.append(response['id'])
            child_category(cat_id=category_id,parent_id=row[0],subname=row[1])
        print(id_list)

    finally:
        cnx.close()



def child_category(cat_id,subname,parent_id:int):
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='localhost',
                                  database='mysql')
    try:
        cursor = cnx.cursor()
        cursor.execute("Select name from categories where parent_id = %s",(parent_id,))
        result = cursor.fetchall()
        for row in result:
            name = row[0]
            data = {
                "name": name,
                "image": {
                    "src": ''
                },
                "parent": cat_id,
            }

            if os.path.exists(f'Useruz/{subname}'):
                pass
            else:
                os.makedirs(f'Useruz/{subname}')
            if  os.path.isfile(f'Useruz/{subname}/{name}.json'):
                print('Subcategory already exists')
                with open(f'Useruz/{subname}/{name}.json', 'r') as f:
                    data = json.load(f)
                    category_id = data['id']
            else:
                response = wcapi.post("products/categories", data).json()
                with open(f'Useruz/{subname}/{name}.json', 'w', encoding='utf-8') as f:
                    json_object = json.dumps(response, indent=4)
                    f.write(json_object)
                    print(f'[cyan]Created json file')
    except Exception as e:
        print(e)



    finally:
        cnx.close()

sub_category()
# child_category(parent_id=2)
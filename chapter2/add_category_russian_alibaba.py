import yaml
import time
from chapter2.create_category_request import send_request_api
import os

from chapter2.replace_chars import replace_chars


def add_category():
    try:
        with open('categories.yaml', 'r') as f:
            data = yaml.safe_load(f)
            # pprint(data)
        for l, category in enumerate(data):
            print(l, category)
            parent_strip = replace_chars(str=category)
            parent_path = f"All/{parent_strip}"
            print("parent_path",parent_path)
            if not os.path.isfile(f'All/{parent_strip}/1.txt'):
                if not os.path.exists(f'All/{parent_strip}'):
                    os.makedirs(f'All/{parent_strip}')
                parent_cat_id = send_request_api(parent_id=2406, path=parent_path,cat_name=category)
                with open(f'All/{parent_strip}/1.txt', 'w') as f:
                    f.write(str(parent_cat_id))
            else:
                print(f'[os]Category {category} already exists')
                with open(f'All/{parent_strip}/1.txt', 'r') as f:
                    id = f.readlines()
                parent_cat_id = id[0]
                print(parent_cat_id)
            for i, subcategory in enumerate(data[category]):
                print(i, subcategory)
                sub_strip = replace_chars(str=subcategory)
                sub_path = f"All/{parent_strip}/{sub_strip}"
                print("sub_path",sub_path)
                if not os.path.isfile(f'All/{parent_strip}/{sub_strip}/1.txt'):
                    if not os.path.exists(f'All/{parent_strip}/{sub_strip}'):
                        os.makedirs(f'All/{parent_strip}/{sub_strip}')
                    subcategory_id = send_request_api(parent_id=parent_cat_id,path=sub_path, cat_name=subcategory)
                    with open(f'All/{parent_strip}/{sub_strip}/1.txt', 'w') as f:
                        f.write(str(subcategory_id))
                else:
                    print(f'[os]Subcategory {subcategory} already exists')
                    with open(f'All/{parent_strip}/{sub_strip}/1.txt', 'r') as f:
                        id = f.readlines()
                    subcategory_id = id[0]
                    print(subcategory_id)
                for k, children in enumerate(data[category][subcategory]):
                    print(k, children)
                    child_strip = replace_chars(str=children)
                    child_path = f"All/{parent_strip}/{sub_strip}/{child_strip}"
                    print("child_path", child_path)
                    if not os.path.isfile(f'All/{parent_strip}/{sub_strip}/{child_strip}/1.txt'):
                        if not os.path.exists(f'All/{parent_strip}/{sub_strip}/{child_strip}'):
                            os.makedirs(f'All/{parent_strip}/{sub_strip}/{child_strip}')

                        children_id = send_request_api(parent_id=subcategory_id, path=child_path,cat_name=children)
                        with open(f'All/{parent_strip}/{sub_strip}/{child_strip}/1.txt', 'w') as f:
                            f.write(str(children_id))
                    else:
                        print(f'[os]Children {children} already exists')
        print('Adding category successfully ended!!!!!!!!!!')
        print('Adding category successfully ended!!!!!!!!!!')
        print('Adding category successfully ended!!!!!!!!!!')
        print('Adding category successfully ended!!!!!!!!!!')
        print('Adding category successfully ended!!!!!!!!!!')
        print('Adding category successfully ended!!!!!!!!!!')
        print('Adding category successfully ended!!!!!!!!!!')
    except Exception as e:
        print(e)
        for i in range(20):
            print(i)
            time.sleep(1)
        add_category()




add_category()
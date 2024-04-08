import os
import json
i = 0
def categories():
    global i
    data_list = []
    Categories = os.listdir('Content/Top categories')
    parent_category_path = os.path.join('Content', 'Top categories')
    with open('Content/Top categories/Response.json', 'r', encoding='utf8') as f:
        data = json.load(f)
        parent_category_id = data['id']
        print("par",parent_category_id)

        for category in Categories:
            if os.path.isdir(os.path.join('Content/Top categories', category)):
                if category == ('- Theory'):
                    pass
                else:
                    sub_category_path = os.path.join(parent_category_path,category)
                    Subcategory_listdir = os.listdir(sub_category_path)
                    with open(f'{sub_category_path}/Response.json', 'r', encoding='utf8') as f:
                        data = json.load(f)
                        sub_category_id = data['id']
                        print("sub",sub_category_id)

                    for sub_category in Subcategory_listdir:
                        child_category_path = os.path.join(sub_category_path,sub_category)
                        if os.path.isdir(child_category_path):
                            if category == ('- Theory'):
                                pass
                            else:
                                i = i + 1
                                with open(f'{child_category_path}/Response.json', 'r', encoding='utf8') as f:
                                    data = json.load(f)
                                    try:
                                        child_category_id = data['id']
                                    except :
                                        child_category_id = data['data']['resource_id']
                                    data_list.append({i:{
                                        'parent_category_id': parent_category_id,
                                        'sub_category_id': sub_category_id,
                                        'child_category_id': child_category_id,
                                    }})
                                with open(f'Category_number.json', 'w', encoding='utf8') as f:
                                    json_data = json.dumps(data_list,indent=4,ensure_ascii=False)
                                    f.write(json_data)










categories()
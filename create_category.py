import os

from WooCommerce_functions import create_category
from url_text import create_json_response


def find_category(src):
    Categories = os.listdir(src)
    for parent_category in Categories:
        if parent_category == '- Theory':
            continue
        else:
            print(parent_category)
            parent_category_listdir = os.path.join(src, parent_category)
            if os.path.isdir(parent_category_listdir):
                parent_category_id = create_category(category_listdir=parent_category_listdir)
                if os.path.isdir(os.path.join(src, parent_category)):
                    SubCategories = os.listdir(os.path.join(src, parent_category))
                    for sub_category in SubCategories:
                        if sub_category == '- Theory':
                            continue
                        else:
                            if os.path.isdir(os.path.join(parent_category_listdir, sub_category)):
                                print(parent_category_listdir)
                                print(sub_category)
                                sub_category_listdir = os.path.join(parent_category_listdir, sub_category)
                                print(sub_category_listdir)
                                sub_category_id = create_category(category_listdir=sub_category_listdir,
                                                                  cat_id=parent_category_id)
                                SubChildCategories = os.listdir(sub_category_listdir)
                                for sub_child_category in SubChildCategories:
                                    if os.path.isdir(os.path.join(sub_category_listdir, sub_child_category)):
                                        sub_child_category_listdir = os.path.join(sub_category_listdir,
                                                                                  sub_child_category)
                                        print(sub_child_category_listdir)
                                        sub_child_category_id = create_category(
                                            category_listdir=sub_child_category_listdir,
                                            cat_id=sub_category_id, img=True)













find_category('Content')


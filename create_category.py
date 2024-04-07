import os


def find_category(src):
    Categories = os.listdir(src)
    for category in Categories:
        if category == '- Theory list':
            continue
        else:
            category_listdir = os.path.join(src, category)
            print(category_listdir,'list')
            if os.path.isdir(os.path.join(src, category)):
                SubCategories = os.listdir(os.path.join(src, category))
                # print(SubCategories)
                pass





find_category('Content')


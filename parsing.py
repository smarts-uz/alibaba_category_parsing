from bs4 import BeautifulSoup
import os
import json
import requests
from pprint import pprint

from convert_to_ru import convert_ru
from url_text import create_url, create_photo, create_json


def search_html(path):
    html_files = []
    if '/.html' in path:path = path[:-len('/.html')]
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.html'):
                # html_files.append(os.path.join(root, file))
                html_files.append({root:os.path.join(root, file)})
                for d in dirs:dirs.remove(d)
    return html_files

# a = search_html('Content/')
# print(a)
def parsing_alibaba(path):
    html_files=search_html(path=path)
    for line in html_files:
        for dir,html in line.items():
            HtmlFile = open(html, 'r', encoding='utf-8')
            source_code = HtmlFile.read()
            soup = BeautifulSoup(source_code, 'html.parser')
            try:
                json_list = soup.find('textarea',id='local-page-info').text
                jsons = json.loads(json_list)
                with open(f'{dir}/App.json',mode='w',encoding='utf-8') as f:
                    json_object = json.dumps(jsons, indent=4)
                    f.write(json_object)
                for i in jsons['modules']:
                    if i['__ncmsFetchCode'] == 200 and i['componentVersionId'] ==952347:
                        # pprint(i['data']['_fdl_request']['requestCommon']['_fdl_request_thirdCategory']['_serverData']['list'])
                        subcategories = i['data']['_fdl_request']['requestCommon']['_fdl_request_thirdCategory']['_serverData']['list']
                        for subcategory in subcategories:
                            img_url = subcategory['imageUrl']
                            action = subcategory['action']
                            categoryIds = subcategory['categoryIds']
                            level = subcategory['level']
                            title = subcategory['title']
                            titleEn = subcategory['titleEn']
                            src = f'{dir}/{titleEn}'
                            if os.path.exists(src):
                                print(f'Directory Already exists: {src}')
                            else:
                                os.makedirs(src)
                                print(f'Directory Created: {src}')
                            create_json(src=src,subcategory=subcategory)
                            create_url(url=action,src=src,titleEn=titleEn)
                            create_photo(img_url=img_url,src=src,titleEn=titleEn)
                            convert_ru(src=src,name=titleEn)


            except:

                print('Category not found!!!')
                json_list =None



# parsing_alibaba(["Content\\Industrial\\Vehicle Accessories, Electronics, & Tools\Vehicle Accessories, Electronics, & Tools.html"])

# parsing_alibaba(html_files=search_html("Content\Top categories\Apparel"))

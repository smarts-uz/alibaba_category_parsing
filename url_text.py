from rich import print
import requests
def create_url(url,src,titleEn):
    try:
        with open(f'{src}/ALL.url',mode='w',encoding='utf-8') as file:
            a = '{000214A0-0000-0000-C000-000000000046}'
            str = f"""[{a}]
Prop3=19,11
[InternetShortcut]
IDList=
URL={url}
IconIndex=13
HotKey=0
IconFile=C:\\Windows\\System32\\SHELL32.dll"""
            file.write(str)
        print(f'[blue]Created url file:{src}/ALL.url')
    except Exception as e:
        print(e)


def create_photo(img_url,src,titleEn):
    try:
        response = requests.get(f'https:{img_url}')
        if response.status_code == 200:
            with open(f'{src}/{titleEn}.{img_url.split(".")[-1]}', mode='wb') as f:
                f.write(response.content)
                print(f'[yellow]Photo saved:{src}/{img_url.split("/")[-1]}')
        else:
            print('Error while downloading photo!')


    except Exception as e:
        print(e)

import json
def create_json(src,subcategory):
    try:
        with open(f'{src}/All.json', mode='w', encoding='utf-8') as f:
            json_object = json.dumps(subcategory, indent=4)
            f.write(json_object)
            print(f'[cyan]Created json file')
    except Exception as e:
        print(e)

import os
def create_json_response(src,response):
    if os.path.exists(f"{src}/Response.json"):
        print('[yellow]Json file already exists')
    else:
        try:
            with open(f'{src}/Response.json', mode='w', encoding='utf-8') as f:
                json_object = json.dumps(response, indent=4)
                f.write(json_object)
                print(f'[cyan]Created json file')
        except Exception as e:
            print(e)

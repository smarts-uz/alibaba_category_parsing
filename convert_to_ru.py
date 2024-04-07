from googletrans import Translator
import os
def convert_ru(name,src):
    translator = Translator()
    ru_name = translator.translate(name,dest='ru',src='en').text
    if os.path.exists(src):
        with open(f"{src}/ru.txt",mode='w',encoding='utf-8') as f:
            f.write(f"{ru_name}")
        print(f'{name} translated to {ru_name} and created {src}/ru.txt')


#
# convert_ru('Fashion & Beaty',src='')

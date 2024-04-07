from googletrans import Translator

def convert_ru(name,src):
    translator = Translator()
    ru_name = translator.translate(name,dest='ru',src='en').text
    print(ru_name)
    with open(f"{src}/{ru_name}.txt",mode='w',encoding='utf-8') as f:
        f.write(ru_name)
    print(f'{name} translated to {ru_name} and created {ru_name}.txt')


#
# convert_ru('Fashion & Beaty',src='')

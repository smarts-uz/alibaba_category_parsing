import os
import regex
import subprocess
import sys
def mhtml_search(path):
    html_files = []
    if '\\.mhtml' in path:path = path[:-len('\\.mhtml')]
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.mhtml'):
                html_files.append(os.path.join(root, file))
                for d in dirs:dirs.remove(d)

    return html_files

def find_content_location(mhtml_files:list):
    urls = []
    for mhtml_file in mhtml_files:
        with open(mhtml_file, mode="r") as mhtml_f:
            text = mhtml_f.read()
            content_location = regex.findall(r'Snapshot-Content-Location: https:.+', text)[0]
            https_url = regex.findall(r'https:.+', content_location)[0]
            new_dir,ext = os.path.splitext(mhtml_file)
            # dir = mhtml_file.split('\\')
            # print(mhtml_file)
            # del dir[-1]
            # new_dir = '\\'.join(dir)
            urls.append({new_dir:https_url})
    return urls


def run_y2z(urls:list):
    for line in urls:
        for dirs,url in line.items():
            execute = subprocess.Popen(
                [f'C:/Users/Администратор/Desktop/smarts software/Cmdline/y2z/1_2_1/monolith.exe', f'{url}', '-o',f'{dirs}.html'])
            code = execute.wait()
            print(code)

a = mhtml_search('Content/')
urls = find_content_location(mhtml_files=a)
html = run_y2z(urls=urls)





# print(len(a))
from parsing import parsing_alibaba
from search_mhtml import mhtml_search, find_content_location, run_y2z


def run_two_func(src):
    # a = mhtml_search(src)
    # urls = find_content_location(mhtml_files=a)
    # html = run_y2z(urls=urls)
    parsing_alibaba(src)


if __name__ == '__main__':
    run_two_func('Content')
import requests
from bs4 import BeautifulSoup
from downers.dblp_helper import BaseDowner, get_titles

def main_page_to_list(main_url='', first_name='', second_name=''):
    # 返回对于这个主界面的子页面的东西
    # search_url_list [url, first_name , second_name ,year]
    search_url_list = []
    req = requests.get(url=main_url)
    html = req.text
    bf = BeautifulSoup(html)

    ul_tag = bf.find_all('ul')[-6]  # 这个-6是实际的结果

    for li in ul_tag.find_all('li'):
        year = (li.a.string).split(' ')[-1]  # 去掉最后的东西
        url = li.a['href']
        search_url_list.append([url, first_name, second_name, year])

    return search_url_list




def main():
    main_page_url = 'https://dblp.uni-trier.de/db/journals/tip/'
    name = 'tip'

    search_url_list = main_page_to_list(main_url=main_page_url,
                                        first_name=name.upper())
    aiDowner = BaseDowner(name, search_url_list)
    aiDowner.start_down_all()

    get_titles(name)


if __name__ == '__main__':
    main()

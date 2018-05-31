import re
from urllib import parse

from bs4 import BeautifulSoup

# 网页解析器，使用BeautifulSoup
class HtmlParser():

    # 每个词条中，可以有多个超链接
    # main_url指url公共部分，如“https://baike.baidu.com/”
    def _get_new_url(self, main_url, soup):
        # baike.baidu.com/
        # <a target="_blank" href="/item/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%E8%AF%AD%E8%A8%80">计算机程序设计语言</a>
        new_urls = set()

        # 解析出main_url之后的url部分
        child_urls = soup.find_all('a', href=re.compile(r'/item/(\%\w{2})+'))
        for child_url in child_urls:
            new_url = child_url['href']

            # 再拼接成完整的url
            full_url = parse.urljoin(main_url, new_url)
            new_urls.add(full_url)
        return new_urls

    # 每个词条中，只有一个描述内容，解析出数据（词条，内容）
    def _get_new_data(self, main_url, soup):
        new_datas = {}
        new_datas['url'] = main_url
        # <dd class="lemmaWgt-lemmaTitle-title"><h1>计算机程序设计语言</h1>...
        new_datas['title'] = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1').get_text()
        # class="lemma-summary" label-module="lemmaSummary"...
        new_datas['content'] = soup.find('div', attrs={'label-module': 'lemmaSummary'},
                                         class_='lemma-summary').get_text()
        return new_datas

    # 解析出url和数据（词条，内容）
    def parse(self, main_url, html_cont):
        if main_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'lxml', from_encoding='utf-8')
        new_url = self._get_new_url(main_url, soup)
        new_data = self._get_new_data(main_url, soup)
        return new_url, new_data

from crawler_test.html_downloader import UrlDownLoader
from crawler_test.html_outer import HtmlOuter
from crawler_test.html_parser import HtmlParser
from crawler_test.url_manager import UrlManager

# 爬虫主程序入口
class MainCrawler():
    def __init__(self):
        # 初始值，实例化四大处理器：url管理器，下载器，解析器，输出器
        self.urls = UrlManager()
        self.downloader = UrlDownLoader()
        self.parser = HtmlParser()
        self.outer = HtmlOuter()

    # 开始爬虫方法
    def start_craw(self, main_url):
        print('爬虫开始...')
        count = 1
        self.urls.add_new_url(main_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('爬虫%d,%s' % (count, new_url))
                html_cont = self.downloader.down_load(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)

                # 将解析出的url放入url管理器，解析出的数据放入输出器中
                self.urls.add_new_urls(new_urls)
                self.outer.conllect_data(new_data)

                if count >= 10:
                    break
                count += 1
            except:
                print('爬虫失败一条')

        self.outer.output()
        print('爬虫结束。')


if __name__ == '__main__':
    main_url = 'https://baike.baidu.com/item/Python/407313'
    mc = MainCrawler()
    mc.start_craw(main_url)

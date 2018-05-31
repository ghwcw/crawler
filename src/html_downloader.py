from urllib import request

# 网页下载器
class UrlDownLoader():
    def down_load(self, url):
        if url is None:
            return None
        else:
            rt = request.Request(url=url, method='GET')     # 发GET请求
            with request.urlopen(rt) as rp:                 # 打开网页
                if rp.status != 200:
                    return None
                else:
                    return rp.read()                        # 读取网页内容

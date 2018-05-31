# 输出器
class HtmlOuter():
    def __init__(self):
        self.datas = []

    # 先收集数据
    def conllect_data(self, data):
        if data is None:
            return
        self.datas.append(data)
        return self.datas

    # 输出为HTML
    def output(self, file='output_html.html'):
        with open(file, 'w', encoding='utf-8') as fh:
            fh.write('<html>')
            fh.write('<head>')
            fh.write('<meta charset="utf-8"></meta>')
            fh.write('<title>爬虫数据结果</title>')
            fh.write('</head>')
            fh.write('<body>')

            fh.write(
                '<table style="border-collapse:collapse; border:1px solid gray; width:80%; word-break:break-all; margin:20px auto;">')
            fh.write('<tr>')
            fh.write('<th style="border:1px solid black; width:35%;">URL</th>')
            fh.write('<th style="border:1px solid black; width:15%;">词条</th>')
            fh.write('<th style="border:1px solid black; width:50%;">内容</th>')
            fh.write('</tr>')
            for data in self.datas:
                fh.write('<tr>')
                fh.write('<td style="border:1px solid black">{0}</td>'.format(data['url']))
                fh.write('<td style="border:1px solid black">{0}</td>'.format(data['title']))
                fh.write('<td style="border:1px solid black">{0}</td>'.format(data['content']))
                fh.write('</tr>')
            fh.write('</table>')

            fh.write('</body>')
            fh.write('</html>')

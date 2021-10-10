#coding:utf-8
import time
import aiohttp
import asyncio
from lxml import etree

# async def get_request(url):
#     print('正在请求的url：',url)
#     time.sleep(2) #time是不支持异步的函数，特征函数中不能出现不支持异步的调用
#     print('请求结束：',url)
#     return 'sabo'

async def get_request(url):
    print('正在请求的url:', url)
    async with aiohttp.ClientSession() as sess:
        ## 阻塞操作前加await关键字
        async with sess.get(url=url) as response:
            page_text = await response.text()
            return page_text

def parse(t):
    page_text = t.result()
    tree = etree.HTML(page_text)
    parse_text = tree.xpath('//dev/text()')
    print(parse_text)

urls=[
    'http://www.baidu.com',
    'http://www.tencent.com',
    'http://www.sohu.com'
]

if __name__ == '__main__':
    start = time.time()
    tasks = []
    for url in urls:
        c = get_request(url)
        task = asyncio.ensure_future(c)
        task.add_done_callback(parse)
        tasks.append(task)

    loop = asyncio.get_event_loop()
    #必须使用wait方法对tasks进行封装才可以
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - start)


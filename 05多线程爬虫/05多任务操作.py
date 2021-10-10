#coding:utf-8
import time
import requests
import asyncio

# async def get_request(url):
#     print('正在请求的url：',url)
#     time.sleep(2) #time是不支持异步的函数，特征函数中不能出现不支持异步的调用
#     print('请求结束：',url)
#     return 'sabo'

async def get_request(url):
    print('正在请求的url:', url)
    await asyncio.sleep(2) ##真正异步操作
    print('请求结果:',url)
    return 'sabo'

urls=[
    'www.baidu.com',
    'www.tencent.com',
    'www.sohu.com'
]

if __name__ == '__main__':
    start = time.time()
    tasks = []
    for url in urls:
        c = get_request(url)
        task = asyncio.ensure_future(c)
        tasks.append(task)

    loop = asyncio.get_event_loop()
    #必须使用wait方法对tasks进行封装才可以
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - start)


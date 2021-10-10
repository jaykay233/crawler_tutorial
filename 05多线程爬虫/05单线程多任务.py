import asyncio
import requests
import time

async def get_request(url):
    print("正在请求的url",url)
    time.sleep(2)
    print("请求结束",url)
    return 'sabo'

def task_callback(t):
    '''
    :param t: 该回调函数的调用者,是唯一的一个参数
    :return:
    '''
    print("i am task_callback(),参数t",t)
    print('t.result()返回的是：', t.result())

if __name__ == '__main__':
    ## c是一个协程对象
    c = get_request('www.baidu.com')

    ## 任务对象就是协程对象的进一步封装
    task = asyncio.ensure_future(c)
    ## 给task绑定一个回调函数
    task.add_done_callback(task_callback)
    ## 创建事件循环对象
    loop = asyncio.get_event_loop()
    ## 将任务注册到事件循环中并且开启事件循环
    loop.run_until_complete(task)

    print(c)
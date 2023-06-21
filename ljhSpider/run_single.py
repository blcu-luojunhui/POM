from api_functions import run_spider, PyRedis

request_obj = {"url": "https://www.baidu.com", "method": "GET"}
redis_key = "Temp:start_urls"
R = PyRedis(key=redis_key)
R.r_push([request_obj])
print("数据存入redis队列")
run_spider(redis_key)
print("爬取完成")

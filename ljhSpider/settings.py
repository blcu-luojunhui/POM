# project basic info
BOT_NAME = "ljhSpider"
SPIDER_MODULES = ["ljhSpider.spiders"]
NEWSPIDER_MODULE = "ljhSpider.spiders"


# Obey robots.txt rules
ROBOTSTXT_OBEY = False
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# use_scrapy_redis
# Enable and configure the scheduler
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# Ensure all spiders share the same duplicates filter through Redis
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# Use Redis-based queue for requests
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"

# Don't clean up Redis queues, allows to pause/resume crawls
SCHEDULER_PERSIST = True

# settings.py
SCHEDULER_SERIALIZER = "scrapy_redis.picklecompat"


# Specify the host and port to use when connecting to Redis
REDIS_URL = "redis://:ljhredis@localhost:6379/1"

# Optional: use a custom queue class
# SCHEDULER_QUEUE_CLASS = 'myproject.myqueue.MyQueue'

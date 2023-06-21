import json
import redis


class PyRedis:
    def __init__(self, key):
        self.redis_connect = redis.StrictRedis(
            host="localhost", port=6379, password="ljhredis", db=1
        )
        self.redis_key = key

    def l_push(self, request_list):
        for req in request_list:
            self.redis_connect.lpush(self.redis_key, json.dumps(req))

    def r_push(self, request_list):
        for req in request_list:
            self.redis_connect.rpush(self.redis_key, json.dumps(req))

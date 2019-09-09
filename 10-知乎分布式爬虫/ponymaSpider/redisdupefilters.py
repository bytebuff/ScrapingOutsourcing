import redis
from scrapy.dupefilters import BaseDupeFilter
from scrapy.utils.request import request_fingerprint


class RedisDupeFilter(BaseDupeFilter):

    def __init__(self, redis_host, redis_port, redis_db):
        print('我是初始化函数__init__')
        # self.fingerprints = set() # 集合(内存)
        # 链接Redis
        self.redis_cli = redis.StrictRedis(
            host=redis_host,
            port=redis_port,
            db=redis_db,)

    # 读取配置文件中数据的 
    # 一般可以读取数据库配置信息
    @classmethod
    def from_settings(cls, settings):
        print('我是配置文件函数from_settings')
        redis_host = settings.get('REDISHOST')
        redis_port = settings.get('REDISPORT')
        redis_db = settings.get('REDISDB')

        return cls(
            redis_host=redis_host,
            redis_port=redis_port,
            redis_db=redis_db
        )

    # 把指纹放到Redis中 并且判断是否已存在
    def request_seen(self, request):
        # 做成指纹
        fp = self.request_fingerprint(request)
        # 判断
        if not self.redis_cli.sismember('dupefilters', fp):
            self.redis_cli.sadd('dupefilters', fp)
            return False
        # 存在就直接返回True
        return True

    # 产生指纹的
    def request_fingerprint(self, request):
        return request_fingerprint(request)

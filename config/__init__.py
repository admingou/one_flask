from redis import StrictRedis
from one_all_web.config.config import redis_host,redis_port,redis_db

redis_store = StrictRedis(host=redis_host, port=redis_port, db=redis_db, decode_responses=True)
#rceate redis client
#retry mechanism for redis client
from tenacity import retry, stop_after_attempt, wait_fixed
import redis.asyncio as redis
import os
from dotenv import load_dotenv
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path)
class RedisClient:
    
    def __init__(self):
        host = os.getenv("redis_host")
        port = int(os.getenv("redis_port"))   
        #logical database number, default is 0     
        self.client = redis.Redis(host=host, port=port, db=0, decode_responses=True)

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    async def set(self, key, value):
        await self.client.set(key, value)

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    async def get(self, key):
        return await self.client.get(key)
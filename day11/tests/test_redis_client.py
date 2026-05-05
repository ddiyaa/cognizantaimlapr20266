import sys
import os
import pytest

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'src')
)
sys.path.insert(0, project_root)

from bankingapp.configurations.redis_client import RedisClient


@pytest.mark.asyncio
async def test_redis_client():
    redis_client = RedisClient()

    assert redis_client is not None, "Failed to create Redis client"

    await redis_client.set("test_key", "test_value")

    value = await redis_client.get("test_key")

    assert value == "test_value", "Failed to set or get value from Redis"
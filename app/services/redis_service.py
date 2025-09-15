import json
from app.core.redis import get_redis

def append_chat_history(session_id: str, message: dict):
    """
    Append a chat message to a user's chat history in Redis.

    Args:
        user_id (str): Unique identifier for the user.
        message (dict): Message to store (e.g., {"role": "user", "content": "Hello"}).

    Notes:
        - Stores messages as JSON strings in a Redis list.
        - Key format: "chat:{user_id}".
    """
    key = f"chat:{session_id}"
    redis_client = get_redis()
    redis_client.rpush(key, json.dumps(message))

def get_chat_history(session_id: str):
    """
    Retrieve the full chat history for a user from Redis.

    Args:
        user_id (str): Unique identifier for the user.

    Returns:
        list[dict]: List of messages in chronological order.
    """
    key = f"chat:{session_id}"
    redis_client = get_redis()
    messages = redis_client.lrange(key, 0, -1)
    return [json.loads(msg) for msg in messages]



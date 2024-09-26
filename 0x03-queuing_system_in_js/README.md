# 0x03. Queuing System in JS
## Files
- **dump.rdb**: Redis data file.
- **0-redis_client.js**: Connects to a redis on localhost at port 6379.
- **1-redis_op.js**: Adds a new key-value pair to redis and retrieves the value using its key. 
- **2-redis_op_async.js**: Node Redis client and async operations.
- **4-redis_advanced_op.js**: Creates hash using redis.
- **5-subscriber.js**: Subscribes to a channel using redis and listens for messages on that channel.
- **5-publisher.js**: Sends messages to the channel subscribed to in 5-subscriber.js. 
- **6-job_creator.js**: creates a job using Kue.

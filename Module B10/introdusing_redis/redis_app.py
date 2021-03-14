import redis
import json

r = redis.Redis(host='redis-15942.c135.eu-central-1-1.ec2.cloud.redislabs.com', port=15942, password='LZmeTDtEbDy39SDuGWo7RHhkmBEh2r2w' )

# dict1 = {'key1': 'value1', 'key2': 'value2'}
# r.set('dict1', json.dumps(dict1))
# converted_dict = json.loads(r.get('dict1'))
# print(type(converted_dict))
# print(converted_dict)

r.delete('key1')
print(r.get('key1'))
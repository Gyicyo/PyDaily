"""
    Create At 2024/3/30
    At:14:56 PM
"""
import yaml#pylint: disable=import-error
from pprint import pprint #pylint: disable=wrong-import-order

with open(file='test.yaml', mode='r',encoding='utf-8') as f:
    config = yaml.safe_load(f)

print(config['database']['string'])
print(config['database']['map'])
print(config['database']['map2'])
print(config['database']['list'])
print(config['database']['list2'])

import sys
sys.path.insert(0, '..')

from app.trifledb_client import TrifleDBClient

client = TrifleDBClient('localhost', 6789)
print(client.put('key', 'value'))
print(client.get('key'))
print(client.get('blah'))

import json
data = {'name': 'John', 'age': 30, 'city': 'New York'}
json_data = json.dumps(data)
print("JSON data:", json_data)
print("Object data:", json.loads(json_data))
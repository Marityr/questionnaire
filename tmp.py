import json


result = """{'14': '1', '15': '1', '16': '1', '17': '1'}"""
new = {'a': 1, 'w': 4}
a = json.loads(result.replace("'",'"'))

tmp = a.copy()
tmp.update(new)

print(tmp)

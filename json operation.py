import json

data = {'name':'Zahid',
        'age':28,
        'country': 'Bangladesh',
        'is_retired': True
        }

json_encoded_str = json.dumps(data)
print(json_encoded_str)


json_decoded_str =json.loads(json_encoded_str)
print(json_decoded_str)
import json

json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
obj = json.loads(json_text)

massage1 = obj["messages"][0]["message"]
print(massage1)

massage2 = obj["messages"][1]["message"]
print(massage2)
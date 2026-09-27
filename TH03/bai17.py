data = [
    {"name": "A", "score": 7},
    {"name": "B", "score": 9},
    {"name": "A", "score": 8}
]
result = {}
for item in data:
    name = item["name"]
    score = item["score"]
    if name in result:
        result[name].append(score)
    else:
        result[name] = [score]
print(result)

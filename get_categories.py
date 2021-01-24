import json

cat = []

with open("map.json") as jf:
    data = json.load(jf)
    #  c for company
    for c in data:
        if c['categories'] and c['categories'] not in cat:
            cat.append(c.get('categories'))

cat = sorted(cat)
    
for c in cat:
    print(c)

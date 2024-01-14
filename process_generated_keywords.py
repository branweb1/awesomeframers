import json
from jinja2 import Environment, FileSystemLoader

entries = {}

with open('./generated_keywords.txt') as keyword_file:
    for line in keyword_file:
        obj = json.loads(line)
        key,val = list(obj.items())[0]
        entries[key] = val

# sort keywords
keywords = set()

for val in entries.values():
    for kw in val:
        keywords.add(kw.lower())

sorted_keywords = sorted(list(keywords))


kw_to_urls = {}

for url,kws in entries.items():
    for kw in kws:
        lower_kw = kw.lower()
        if lower_kw in kw_to_urls:
            kw_to_urls[lower_kw].append(url)
        else:
            kw_to_urls[lower_kw] = [url]

environment = Environment(loader=FileSystemLoader("./"))

template = environment.get_template("index.j2.html")

with open('./index.html', 'w') as output_file:
    output_file.write(template.render(index=kw_to_urls, sorted_keys=sorted_keywords))



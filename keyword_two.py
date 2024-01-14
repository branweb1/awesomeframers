import json
import re
from jinja2 import Environment, FileSystemLoader

master_group_list = {}

with open('./keyword_output.json') as groups:
    group_list = json.load(groups)
    for group in group_list:
        for k,v in group.items():
            if k in master_group_list:
                print(k)
                master_group_list[k] = list(
                    set(
                        master_group_list[k] + v
                    )
                )
            else:
                master_group_list[k] = v

# invert so it maps keywords to group
group_mapping = {}
for k,vs in master_group_list.items():
    for v in vs:
        group_mapping[v] = k

url_mapping = {}

# go through each entry's keywords to make map of group to url
with open('./output.json') as entries:
    for line in entries:
        try:
            entry = json.loads(json.loads(line))
            if 'keywords' in entry:
                for keyword in entry['keywords']:
                    keyword_lc = keyword.lower()
                    if keyword_lc not in group_mapping:
                        snake_case = re.sub(r'\s', '_', keyword_lc)
                        if snake_case in group_mapping:
                            keyword_lc = snake_case
                        else:
                            print(f"MISSING KEYWORD: {keyword_lc}")
                            group_mapping[keyword_lc] = keyword_lc


                    group = group_mapping[keyword_lc]
                    if group in url_mapping:
                        url_mapping[group].append(entry['url'])
                    else:
                        url_mapping[group] = [entry['url']]
        except json.decoder.JSONDecodeError:
            print("decode error")


environment = Environment(loader=FileSystemLoader("./"))

template = environment.get_template("index.j2.html")

with open('./index.html', 'w') as output_file:
    output_file.write(template.render(index=url_mapping, sorted_keys=sorted(list(url_mapping.keys()))))

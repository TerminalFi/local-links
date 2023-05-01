import json

file_path = "/Users/terminal/git/local-links/local_links.txt"


def create_items_list(file_path):
    items = []
    with open(file_path, 'r') as file:
        for line in file:
            link = line.strip()
            arg = link
            if not link.startswith("http"):
                arg = "file://" + link
            items.append({
                "title": link,
                "subtitle": "open",
                "arg": arg
            })
    return items

items_list = create_items_list(file_path)
output = {"items": items_list}

print(json.dumps(output, indent=2))

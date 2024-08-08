import requests
from pprint import pprint
import json


def main():
    url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
    resp = requests.get(url)
    # pprint(resp.json())
    # Анализ структуры данных
    resp_dict = resp.json()
    readable_file = 'readable_file.json'
    with open(readable_file, 'w', encoding='utf-8') as in_file:
        json.dump(resp_dict, in_file, indent=4, ensure_ascii=False)
    with open(readable_file, 'r', encoding='utf-8') as out_file:
        file = json.load(out_file)
        pprint(file)


if __name__ == "__main__":
    main()

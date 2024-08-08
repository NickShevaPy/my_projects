import requests
import json
import jmespath
from pprint import pprint
import asyncio
import httpx
from operator import itemgetter


async def dump_load_url():
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        # print(resp.json())
        submission_ids = resp.json()
        submission_dicts = []
        for i in submission_ids[:5]:
            url = 'https://hacker-news.firebaseio.com/v0/item/' + str(i) + '.json'
            resp_in = await client.get(url)
            resp_dict = resp_in.json()
            submission_dict = {
                "title": resp_dict['title'],
                'link': 'https://news.ycombinator.com/' + str(i),
                'comment': resp_dict.get('descendants')
            }
            submission_dicts.append(submission_dict)
        submission_dicts = sorted(submission_dicts, key=itemgetter('comment'), reverse=True)
        # pprint(submission_dicts)
        # get list of amount of comments
        query = "[*].comment"
        my_search = jmespath.search(query, submission_dicts)
        print(my_search)


if __name__ == "__main__":
    asyncio.run(dump_load_url())

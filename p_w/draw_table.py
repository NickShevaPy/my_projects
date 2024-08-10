from plotly.graph_objects import Bar
from plotly import offline
from hn_submissions import dump_load_url
import jmespath
import asyncio
from dataclasses import dataclass


async def title():
    submission_dicts = await dump_load_url()
    title = "[*].title"
    my_title = jmespath.search(title, submission_dicts)
    return my_title


async def comment():
    submission_dicts = await dump_load_url()
    comment = "[*].comment"
    my_comment = jmespath.search(comment, submission_dicts)
    return my_comment


async def paint():
    # to build visualization
    y = await comment()
    x = await title()
    data = [{
        'type': 'bar',
        'x': x,
        'y': y,
    }]
    my_layout = {
        'title': "Most popular articles",
        'xaxis': {'title': 'Title'},
        'yaxis': {'title': "Comments"}
    }
    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='articles.html')


async def main():
    # task = asyncio.gather(title(), comment(), paint())
    tasks = [title(), comment(), paint()]
    await asyncio.sleep(.2)
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
    # asyncio.run(paint())

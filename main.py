import asyncio
import arguments

import aiohttp


async def request(session, url):
    try:
        async with session.get(url) as response:
            st_code = response.status
            return 199 < st_code < 300
    except aiohttp.ClientConnectorError:
        return False


async def session_request(url):
    async with aiohttp.ClientSession() as session:
        return await request(session, url)


async def main():
    c = 0
    args = arguments.get()

    tasks = []
    for _ in range(args.repeats):
        task = asyncio.create_task(session_request(args.url))
        tasks.append(task)

    for task in tasks:
        await task
        c += await task

    print('Accepted:   {}'.format(c))
    print('Inited:     {}'.format(args.repeats))
    print('Percentage: {} %'.format(round(c / args.repeats * 100)))


if __name__ == '__main__':
    asyncio.run(main())

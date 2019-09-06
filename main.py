import asyncio
import arguments

import aiohttp


async def request(session, url, timeout):
    try:
        async with session.get(url, timeout=timeout) as response:
            st_code = response.status
            return 199 < st_code < 300
    except (aiohttp.ClientConnectorError, asyncio.TimeoutError):
        return False


async def session_request(url, timeout):
    async with aiohttp.ClientSession() as session:
        return await request(session, url, timeout)


async def main():
    c = 0
    args = arguments.get()

    tasks = []
    for _ in range(args.repeats):
        task = asyncio.create_task(session_request(args.url, args.timeout))
        tasks.append(task)

    for task in tasks:
        await task
        c += await task

    print('Accepted:   {}'.format(c))
    print('Inited:     {}'.format(args.repeats))
    print('Percentage: {} %'.format(round(c / args.repeats * 100)))


if __name__ == '__main__':
    asyncio.run(main())

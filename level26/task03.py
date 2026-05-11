import asyncio

async def set_future_result(fut):
    await asyncio.sleep(3)
    fut.set_result('Hello, Future!')

async def main():
    fut = asyncio.Future()
    await asyncio.gather(set_future_result(fut))
    print(fut.result())

asyncio.run(main())
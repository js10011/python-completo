import asyncio

async def set_future_result(future):
    await asyncio.sleep(1)
    future.set_result('Result after 1 second')

async def main():
    loop = asyncio.get_running_loop()
    future = loop.create_future()
    
    await set_future_result(future)
    print(future.result())

asyncio.run(main())